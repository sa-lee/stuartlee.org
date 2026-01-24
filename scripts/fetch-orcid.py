#!/usr/bin/env python3
"""Fetch publications from ORCID and convert to BibTeX.

This script:
1. Fetches work summaries from ORCID public API
2. Extracts DOIs from each work
3. Fetches complete BibTeX entries from doi.org (which has full metadata)
4. Falls back to basic ORCID data if DOI lookup fails

Best practices implemented:
- Rate limiting to respect API quotas (ORCID: 12 req/sec anonymous)
- User-Agent header for API citizenship
- doi.org for complete BibTeX (includes authors, journal, etc.)
- Deduplication by DOI
- Error handling with logging

References:
- https://info.orcid.org/ufaqs/what-are-the-api-limits/
- https://chrisholdgraf.com/blog/2022/orcid-auto-update/
"""

import json
import logging
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime
from typing import Optional

ORCID_ID = "0000-0003-1179-8436"
USER_AGENT = "stuartlee.org-publication-sync/1.0 (https://stuartlee.org)"

# Rate limiting: be conservative to avoid hitting limits
REQUEST_DELAY = 0.2  # 200ms between requests (5 req/sec, well under limits)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def make_request(url: str, accept: str = "application/json") -> Optional[bytes]:
    """Make an HTTP request with proper headers and error handling."""
    headers = {
        "Accept": accept,
        "User-Agent": USER_AGENT,
    }
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return response.read()
    except urllib.error.HTTPError as e:
        logger.warning(f"HTTP error {e.code} for {url}: {e.reason}")
        return None
    except urllib.error.URLError as e:
        logger.warning(f"URL error for {url}: {e.reason}")
        return None
    except TimeoutError:
        logger.warning(f"Timeout for {url}")
        return None


def fetch_orcid_works() -> dict:
    """Fetch works from ORCID public API."""
    url = f"https://pub.orcid.org/v3.0/{ORCID_ID}/works"
    logger.info(f"Fetching works from ORCID: {url}")

    data = make_request(url, accept="application/json")
    if data is None:
        logger.error("Failed to fetch ORCID works")
        return {"group": []}

    return json.loads(data.decode())


def fetch_bibtex_from_doi(doi: str) -> Optional[str]:
    """Fetch BibTeX entry from doi.org.

    This provides complete metadata including authors, journal, volume, etc.
    that ORCID summaries don't include.
    """
    # Clean the DOI (remove any newlines or whitespace)
    doi = doi.strip().replace("\n", "")

    # doi.org resolves DOIs and can return BibTeX via content negotiation
    url = f"https://doi.org/{doi}"

    time.sleep(REQUEST_DELAY)  # Rate limiting

    data = make_request(url, accept="application/x-bibtex")
    if data is None:
        return None

    bibtex = data.decode("utf-8")

    # Clean up common issues in BibTeX from doi.org
    # Some entries have odd formatting
    bibtex = bibtex.strip()

    return bibtex


def extract_doi_from_work(work: dict) -> Optional[str]:
    """Extract DOI from an ORCID work entry."""
    summary = work.get("work-summary", [{}])[0]
    external_ids = summary.get("external-ids", {}).get("external-id", [])

    for ext_id in external_ids:
        if ext_id.get("external-id-type") == "doi":
            return ext_id.get("external-id-value")

    return None


def work_to_basic_bibtex(work: dict) -> Optional[str]:
    """Convert ORCID work to basic BibTeX entry (fallback when DOI lookup fails)."""
    try:
        summary = work["work-summary"][0]
        title = summary["title"]["title"]["value"]
        pub_date = summary.get("publication-date") or {}
        year = pub_date.get("year", {}).get("value", "")

        # Get DOI if available
        doi = extract_doi_from_work(work) or ""

        # Create a citation key from put-code
        key = f"orcid_{summary['put-code']}"

        # Get work type for entry type
        work_type = summary.get("type", "journal-article")
        entry_type = "article"  # Default
        if work_type in ["book", "edited-book"]:
            entry_type = "book"
        elif work_type == "book-chapter":
            entry_type = "incollection"
        elif work_type in ["conference-paper", "conference-abstract"]:
            entry_type = "inproceedings"

        entry = f"""@{entry_type}{{{key},
  title = {{{title}}},
  year = {{{year}}},
  doi = {{{doi}}},
  note = {{Retrieved from ORCID}}
}}"""
        return entry
    except (KeyError, TypeError, IndexError) as e:
        logger.warning(f"Failed to create basic BibTeX: {e}")
        return None


def normalize_bibtex_key(bibtex: str, doi: str) -> str:
    """Normalize BibTeX citation key to be based on DOI for consistency."""
    # Create a safe key from DOI
    safe_key = re.sub(r"[^a-zA-Z0-9]", "_", doi)

    # Replace the existing key
    # BibTeX format: @type{key,
    pattern = r"@(\w+)\{[^,]+,"
    replacement = f"@\\1{{{safe_key},"

    return re.sub(pattern, replacement, bibtex, count=1)


def main():
    """Main function to fetch and write publications."""
    works_data = fetch_orcid_works()
    groups = works_data.get("group", [])

    logger.info(f"Found {len(groups)} work groups in ORCID")

    entries = []
    seen_dois = set()  # For deduplication

    for i, group in enumerate(groups):
        doi = extract_doi_from_work(group)

        if doi:
            # Normalize DOI for deduplication
            doi_lower = doi.lower().strip()
            if doi_lower in seen_dois:
                logger.info(f"Skipping duplicate DOI: {doi}")
                continue
            seen_dois.add(doi_lower)

            logger.info(f"[{i+1}/{len(groups)}] Fetching BibTeX for DOI: {doi}")
            bibtex = fetch_bibtex_from_doi(doi)

            if bibtex:
                # Normalize the citation key
                bibtex = normalize_bibtex_key(bibtex, doi)
                entries.append(bibtex)
                continue

        # Fallback to basic ORCID data
        logger.info(f"[{i+1}/{len(groups)}] Using basic ORCID data (no DOI or DOI lookup failed)")
        basic_entry = work_to_basic_bibtex(group)
        if basic_entry:
            entries.append(basic_entry)

    if not entries:
        logger.warning("No entries to write")
        sys.exit(0)

    # Write to references.bib
    output_path = "references.bib"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"% Auto-generated from ORCID ({ORCID_ID}) on {datetime.now().isoformat()}\n")
        f.write(f"% Source: https://orcid.org/{ORCID_ID}\n")
        f.write(f"% BibTeX fetched from doi.org for complete metadata\n\n")
        f.write("\n\n".join(entries))
        f.write("\n")

    logger.info(f"Wrote {len(entries)} entries to {output_path}")


if __name__ == "__main__":
    main()
