# Quarto Migration Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Migrate stuartlee.org from Hugo/blogdown to Quarto with GitHub Actions auto-deploy to SiteGround.

**Architecture:** Quarto website with built-in theme + custom SCSS, BibTeX-driven publications page with ORCID auto-sync, GitHub Actions pipeline using ssh-agent for passphrase-protected key deployment via rsync.

**Tech Stack:** Quarto, SCSS, GitHub Actions, rsync, ORCID API, BibTeX

---

### Task 1: Initialize Quarto Project

**Files:**
- Create: `_quarto.yml`
- Create: `.gitignore` (update)

**Step 1: Create Quarto configuration**

```yaml
project:
  type: website
  output-dir: _site

website:
  title: "Stuart Lee"
  description: "Personal website of Stuart Lee - data science, visualization, and software"
  site-url: https://stuartlee.org

  navbar:
    left:
      - text: About
        href: about.qmd
      - text: Writing
        href: posts.qmd
      - text: Publications
        href: publications.qmd
      - text: CV
        href: cv.qmd
    right:
      - icon: github
        href: https://github.com/sa-lee
      - icon: envelope
        href: contact.qmd

  page-footer:
    center: "© 2017-2026 Stuart Lee"

format:
  html:
    theme:
      light: cosmo
    css: styles.scss
    toc: true

execute:
  freeze: auto
```

**Step 2: Update .gitignore**

Add to `.gitignore`:
```
_site/
_freeze/
.quarto/
/.quarto/
```

**Step 3: Verify files created**

Run: `ls -la _quarto.yml && cat _quarto.yml`
Expected: File exists with content above

**Step 4: Commit**

```bash
git add _quarto.yml .gitignore
git commit -m "feat: initialize Quarto project configuration"
```

---

### Task 2: Create Base Pages

**Files:**
- Create: `index.qmd`
- Create: `about.qmd`
- Create: `contact.qmd`
- Create: `posts.qmd`

**Step 1: Create homepage**

Create `index.qmd`:
```markdown
---
title: "Stuart Lee"
subtitle: "Data Science | Visualization | Software"
page-layout: full
---

Hi, I'm Stuart! I'm a researcher focused on human-centred approaches to data science.

My work explores how we can use computation and visualisation to augment the exploration of data and models.

[About me](about.qmd){.btn .btn-primary} [Publications](publications.qmd){.btn .btn-secondary}
```

**Step 2: Migrate about page**

Create `about.qmd`:
```markdown
---
title: "Who?"
---

Hi, I'm Stuart! I'm a post-doctoral research fellow at Monash University in the Department of Econometrics and Business Statistics. My research focuses on
human centred approaches to data science -- how can we
use computation and visualisation to augment the exploration of data and models? How do we perform inference with exploratory visualisations?
I am a big believer in using [interactive](https://github.com/vegawidget/virgo) and [dynamic](https://github.com/ggobi/tourr) graphics to achieve these goals.

I am also interested the process and "science" of doing data science - how can
we experiment with black box models and algorithms to understand how they work? What makes an effective data analysis? When can we say we've learned something new and true about the world from an analysis?

I want to make data science more accessible to people
without quantitative or programming backgrounds, which has led me to think
a lot about software design and teaching statistics and R.

Outside of research I enjoy:

* Coffee - both the making and drinking of.
* Cooking.
* Board Games, especially co-op ones.
* Hiking.
```

**Step 3: Migrate contact page**

Create `contact.qmd`:
```markdown
---
title: "Contact"
---

Feel free to get in touch with me - you can find me on the internet at these places:

- Email: hello at stuartlee.org
- [GitHub](https://github.com/sa-lee)
- [Mastodon](https://fosstodon.org/@stuartlee)
```

**Step 4: Create posts listing page**

Create `posts.qmd`:
```markdown
---
title: "Writing"
listing:
  contents: posts
  sort: "date desc"
  type: default
  categories: true
  feed: true
---
```

**Step 5: Verify pages**

Run: `ls -la *.qmd`
Expected: index.qmd, about.qmd, contact.qmd, posts.qmd

**Step 6: Commit**

```bash
git add index.qmd about.qmd contact.qmd posts.qmd
git commit -m "feat: add base pages (home, about, contact, posts listing)"
```

---

### Task 3: Create Publications Page with BibTeX

**Files:**
- Create: `references.bib`
- Create: `publications.qmd`

**Step 1: Create BibTeX file**

Create `references.bib` with Stuart's publications:
```bibtex
@article{lee2020casting,
  author = {Lee, Stuart and Laa, Ursula and Cook, Dianne},
  title = {Casting Multiple Shadows: High-Dimensional Interactive Data Visualisation with Tours and Embeddings},
  journal = {arXiv preprint arXiv:2012.06077},
  year = {2020},
  url = {http://arxiv.org/abs/2012.06077}
}

@article{laa2020burning,
  author = {Laa, Ursula and Cook, Dianne and Lee, Stuart},
  title = {Burning sage: Reversing the curse of dimensionality in the visualization of high-dimensional data},
  journal = {arXiv preprint arXiv:2009.10979},
  year = {2020},
  url = {http://arxiv.org/abs/2009.10979}
}

@article{lee2020fluent,
  author = {Lee, Stuart and Lawrence, Michael and Love, Michael I.},
  title = {Fluent genomics with plyranges and tximeta},
  journal = {F1000Research},
  volume = {9},
  number = {109},
  pages = {109},
  year = {2020},
  doi = {10.12688/f1000research.22259.1}
}

@article{lee2019plyranges,
  author = {Lee, Stuart and Cook, Dianne and Lawrence, Michael},
  title = {plyranges: a grammar of genomic data transformation},
  journal = {Genome Biology},
  volume = {20},
  number = {1},
  pages = {4},
  year = {2019},
  doi = {10.1186/s13059-018-1597-8}
}

@article{henden2018identity,
  author = {Henden, Lyndal and Lee, Stuart and Mueller, Ivo and Barry, Alyssa and Bahlo, Melanie},
  title = {Identity-by-descent analyses for measuring population dynamics and selection in recombining pathogens},
  journal = {PLoS Genetics},
  volume = {14},
  number = {5},
  pages = {e1007279},
  year = {2018},
  doi = {10.1371/journal.pgen.1007279}
}
```

**Step 2: Create publications page**

Create `publications.qmd`:
```markdown
---
title: "Publications"
bibliography: references.bib
nocite: |
  @*
csl: apa.csl
---

Here are some of my recent papers and preprints. You can find more at my [ORCiD](https://orcid.org/0000-0003-1179-8436) and [Google Scholar](https://scholar.google.com/citations?user=793ayD4AAAAJ&hl=en) pages.

::: {#refs}
:::
```

**Step 3: Download APA citation style**

Run: `curl -o /home/stuart/stuartlee.org/apa.csl https://raw.githubusercontent.com/citation-style-language/styles/master/apa.csl`

**Step 4: Verify files**

Run: `ls -la references.bib publications.qmd apa.csl`
Expected: All three files exist

**Step 5: Commit**

```bash
git add references.bib publications.qmd apa.csl
git commit -m "feat: add publications page with BibTeX support"
```

---

### Task 4: Migrate Blog Posts

**Files:**
- Create: `posts/_metadata.yml`
- Create: `posts/2018-04-16-rookie/index.qmd`
- Create: `posts/2019-07-02-s4/index.qmd`
- Create: `posts/2020-06-17-mida/index.qmd`
- Copy: image assets from old posts

**Step 1: Create posts directory and metadata**

Run: `mkdir -p posts`

Create `posts/_metadata.yml`:
```yaml
freeze: auto
```

**Step 2: Migrate rookie-mistakes post**

Create `posts/2018-04-16-rookie/index.qmd` - copy content from existing post, update frontmatter:
```yaml
---
title: "Rookie mistakes and how to fix them when making plots of data"
author: "Stuart Lee, Di Cook"
date: "2018-04-14"
categories: [education, statistical-graphics, data-visualisation, R, ggplot2]
---
```

Copy images: `cp -r content/post/2018-04-16-rookie/index_files posts/2018-04-16-rookie/`

**Step 3: Migrate s4 post**

Create `posts/2019-07-02-s4/index.qmd` with updated frontmatter.
Copy images: `cp -r content/post/2019-07-02-s4/img posts/2019-07-02-s4/`

**Step 4: Migrate mida post**

Create `posts/2020-06-17-mida/index.qmd` with updated frontmatter.
Copy images: `cp content/post/2020-06-17-mida/*.png posts/2020-06-17-mida/`

**Step 5: Verify posts structure**

Run: `find posts -type f | head -20`
Expected: index.qmd files and image assets in each post directory

**Step 6: Commit**

```bash
git add posts/
git commit -m "feat: migrate blog posts to Quarto format"
```

---

### Task 5: Create Custom Styling

**Files:**
- Create: `styles.scss`

**Step 1: Create SCSS file**

Create `styles.scss`:
```scss
/*-- scss:defaults --*/

// Fonts
$font-family-sans-serif: "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
$font-family-monospace: "Fira Code", "Source Code Pro", monospace;

// Colors - professional academic palette
$primary: #2c3e50;
$link-color: #3498db;

/*-- scss:rules --*/

// Cleaner headings
h1, h2, h3, h4, h5, h6 {
  font-weight: 600;
  margin-top: 1.5rem;
}

// Better code blocks
pre {
  border-radius: 0.5rem;
  padding: 1rem;
}

// Homepage styling
.quarto-title-block {
  margin-bottom: 2rem;
}

// Footer
.nav-footer {
  margin-top: 3rem;
}
```

**Step 2: Verify file**

Run: `cat styles.scss`
Expected: SCSS content as above

**Step 3: Commit**

```bash
git add styles.scss
git commit -m "feat: add custom SCSS styling"
```

---

### Task 6: Create GitHub Actions Deploy Workflow

**Files:**
- Create: `.github/workflows/deploy.yml`

**Step 1: Create workflow directory**

Run: `mkdir -p .github/workflows`

**Step 2: Create deploy workflow**

Create `.github/workflows/deploy.yml`:
```yaml
name: Deploy to SiteGround

on:
  push:
    branches: [master]
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Render site
        run: quarto render

      - name: Setup SSH with passphrase
        env:
          SSH_PRIVATE_KEY: ${{ secrets.SITEGROUND_SSH_KEY }}
          SSH_PASSPHRASE: ${{ secrets.SITEGROUND_SSH_PASSPHRASE }}
          SSH_HOST: ${{ secrets.SITEGROUND_HOST }}
        run: |
          mkdir -p ~/.ssh
          echo "$SSH_PRIVATE_KEY" > ~/.ssh/deploy_key
          chmod 600 ~/.ssh/deploy_key

          # Add host to known_hosts
          ssh-keyscan -p ${{ secrets.SITEGROUND_PORT }} $SSH_HOST >> ~/.ssh/known_hosts

          # Start ssh-agent and add key with passphrase
          eval $(ssh-agent -s)
          echo "$SSH_PASSPHRASE" | setsid ssh-add ~/.ssh/deploy_key 2>/dev/null || \
            expect -c "spawn ssh-add ~/.ssh/deploy_key; expect \"passphrase\"; send \"$SSH_PASSPHRASE\r\"; expect eof" || \
            SSH_ASKPASS_REQUIRE=force SSH_ASKPASS="echo $SSH_PASSPHRASE" ssh-add ~/.ssh/deploy_key

      - name: Deploy via rsync
        env:
          SSH_HOST: ${{ secrets.SITEGROUND_HOST }}
          SSH_USER: ${{ secrets.SITEGROUND_USER }}
          SSH_PORT: ${{ secrets.SITEGROUND_PORT }}
        run: |
          eval $(ssh-agent -s)
          echo "${{ secrets.SITEGROUND_SSH_PASSPHRASE }}" | SSH_ASKPASS_REQUIRE=force SSH_ASKPASS="cat" ssh-add ~/.ssh/deploy_key

          rsync -avz --delete \
            -e "ssh -p $SSH_PORT -o StrictHostKeyChecking=no" \
            _site/ \
            ${SSH_USER}@${SSH_HOST}:~/www/stuartlee.org/public_html/
```

**Step 3: Verify workflow**

Run: `cat .github/workflows/deploy.yml`
Expected: YAML content as above

**Step 4: Commit**

```bash
git add .github/workflows/deploy.yml
git commit -m "feat: add GitHub Actions deploy workflow for SiteGround"
```

---

### Task 7: Create ORCID Sync Workflow

**Files:**
- Create: `.github/workflows/sync-orcid.yml`
- Create: `scripts/fetch-orcid.py`

**Step 1: Create scripts directory**

Run: `mkdir -p scripts`

**Step 2: Create ORCID fetch script**

Create `scripts/fetch-orcid.py`:
```python
#!/usr/bin/env python3
"""Fetch publications from ORCID and convert to BibTeX."""

import json
import urllib.request
from datetime import datetime

ORCID_ID = "0000-0003-1179-8436"

def fetch_orcid_works():
    """Fetch works from ORCID public API."""
    url = f"https://pub.orcid.org/v3.0/{ORCID_ID}/works"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode())

def work_to_bibtex(work):
    """Convert ORCID work to BibTeX entry."""
    summary = work["work-summary"][0]
    title = summary["title"]["title"]["value"]
    year = summary.get("publication-date", {}).get("year", {}).get("value", "")

    # Get external IDs
    doi = ""
    for ext_id in summary.get("external-ids", {}).get("external-id", []):
        if ext_id["external-id-type"] == "doi":
            doi = ext_id["external-id-value"]
            break

    # Create citation key
    key = f"orcid_{summary['put-code']}"

    entry = f"""@article{{{key},
  title = {{{title}}},
  year = {{{year}}},
  doi = {{{doi}}}
}}
"""
    return entry

def main():
    works = fetch_orcid_works()

    entries = []
    for group in works.get("group", []):
        try:
            entry = work_to_bibtex(group)
            entries.append(entry)
        except (KeyError, TypeError):
            continue

    # Write to references.bib
    with open("references.bib", "w") as f:
        f.write(f"% Auto-generated from ORCID on {datetime.now().isoformat()}\n\n")
        f.write("\n".join(entries))

    print(f"Wrote {len(entries)} entries to references.bib")

if __name__ == "__main__":
    main()
```

**Step 3: Create sync workflow**

Create `.github/workflows/sync-orcid.yml`:
```yaml
name: Sync ORCID Publications

on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly on Sunday
  workflow_dispatch:

jobs:
  sync:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Fetch ORCID publications
        run: python scripts/fetch-orcid.py

      - name: Commit changes
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add references.bib
          git diff --staged --quiet || git commit -m "chore: sync publications from ORCID"
          git push
```

**Step 4: Verify files**

Run: `ls -la scripts/fetch-orcid.py .github/workflows/sync-orcid.yml`

**Step 5: Commit**

```bash
git add scripts/fetch-orcid.py .github/workflows/sync-orcid.yml
git commit -m "feat: add ORCID publications sync workflow"
```

---

### Task 8: Create CV Page

**Files:**
- Create: `cv.qmd`

**Step 1: Create CV page**

Create `cv.qmd`:
```markdown
---
title: "CV"
---

## Stuart Lee

**Post-doctoral Research Fellow**
Department of Econometrics and Business Statistics
Monash University

[Email](mailto:hello@stuartlee.org) | [GitHub](https://github.com/sa-lee) | [ORCiD](https://orcid.org/0000-0003-1179-8436)

---

## Research Interests

- Human-centred data science
- Interactive and dynamic data visualization
- Statistical graphics and exploratory data analysis
- Bioinformatics and genomics

---

## Education

*Update this section with your education details*

---

## Experience

*Update this section with your experience*

---

## Software

- [plyranges](https://github.com/sa-lee/plyranges) - A grammar of genomic data transformation
- [virgo](https://github.com/vegawidget/virgo) - Interactive graphics with Vega-Lite
- [tourr](https://github.com/ggobi/tourr) - Tour methods for multivariate data visualization

---

## Publications

See [full publications list](publications.qmd).
```

**Step 2: Commit**

```bash
git add cv.qmd
git commit -m "feat: add CV page"
```

---

### Task 9: Test Local Preview

**Step 1: Install Quarto if needed**

Run: `which quarto || echo "Quarto not installed"`

If not installed, user needs to install from https://quarto.org/docs/get-started/

**Step 2: Render site**

Run: `cd /home/stuart/stuartlee.org && quarto render`
Expected: Site builds to `_site/` directory without errors

**Step 3: Preview site**

Run: `cd /home/stuart/stuartlee.org && quarto preview`
Expected: Local server starts, opens browser at localhost

**Step 4: Verify all pages work**

Manual check:
- Homepage loads
- About page loads
- Publications page shows BibTeX entries
- Posts listing shows 3 posts
- Individual posts render correctly with images
- CV page loads

---

### Task 10: Clean Up Old Hugo Files

**Files:**
- Remove: `config.toml`
- Remove: `content/` directory
- Remove: `layouts/` directory
- Remove: `themes/` directory
- Remove: `Makefile`
- Remove: `static/` directory

**Step 1: Verify Quarto site works**

Run: `quarto render && ls _site/index.html`
Expected: index.html exists

**Step 2: Remove old Hugo files**

```bash
rm -rf content/ layouts/ themes/ static/
rm config.toml Makefile
```

**Step 3: Commit removal**

```bash
git add -A
git commit -m "chore: remove old Hugo/blogdown files"
```

---

### Task 11: Push and Test Deployment

**Step 1: Push to GitHub**

```bash
git push origin master
```

**Step 2: Monitor GitHub Actions**

Go to: https://github.com/sa-lee/stuartlee.org/actions

Expected: Deploy workflow runs and succeeds

**Step 3: Verify live site**

Visit: https://stuartlee.org
Expected: New Quarto site is live

---

## Summary of Files

**New files:**
- `_quarto.yml` - Quarto configuration
- `index.qmd` - Homepage
- `about.qmd` - About page
- `contact.qmd` - Contact page
- `posts.qmd` - Posts listing
- `publications.qmd` - Publications page
- `cv.qmd` - CV page
- `references.bib` - BibTeX publications
- `apa.csl` - Citation style
- `styles.scss` - Custom styling
- `posts/_metadata.yml` - Posts config
- `posts/*/index.qmd` - Migrated posts
- `.github/workflows/deploy.yml` - Deploy workflow
- `.github/workflows/sync-orcid.yml` - ORCID sync
- `scripts/fetch-orcid.py` - ORCID fetch script

**Removed files:**
- `config.toml`
- `content/`
- `layouts/`
- `themes/`
- `static/`
- `Makefile`
