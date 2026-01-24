# Quarto Migration Design

## Overview

Migrate stuartlee.org from Hugo/blogdown to Quarto with automated GitHub Actions deployment to SiteGround.

## Goals

- Fresh content workflow (easier to write and deploy)
- Auto-deploy to SiteGround on push
- Professional appearance
- Easy CV/publications updates (ORCID sync)
- Good security practices
- Multi-language support (not R-dependent)

## Current State

- **Generator**: Hugo via R/blogdown
- **Theme**: Paperesque
- **Content**: 3 blog posts, about/contact/publications pages
- **Deployment**: Manual rsync to SiteGround
- **Last updated**: 2020

## New Architecture

### Project Structure

```
stuartlee.org/
├── _quarto.yml           # Main config
├── index.qmd             # Homepage
├── about.qmd             # About page
├── contact.qmd           # Contact page
├── cv.qmd                # CV (new)
├── publications.qmd      # Publications (BibTeX-driven)
├── references.bib        # Publications in BibTeX
├── posts/                # Blog posts
│   ├── _metadata.yml     # Shared post settings
│   └── [migrated posts]
├── styles.scss           # Custom styling
├── _site/                # Build output (gitignored)
└── .github/
    └── workflows/
        └── deploy.yml    # GitHub Actions
```

### Technology Stack

- **Generator**: Quarto
- **Theme**: Built-in (cosmo/flatly) + custom SCSS
- **Deployment**: GitHub Actions → rsync → SiteGround
- **Publications**: BibTeX with ORCID auto-sync

### Post Workflow

1. Create: `quarto create post "title"`
2. Write: Edit `.qmd` file (supports R, Python, Julia, Observable JS)
3. Preview: `quarto preview`
4. Publish: `git push` (auto-deploys)

### ORCID Publications Sync

GitHub Action runs weekly:
1. Fetches publications from ORCID API
2. Converts to BibTeX
3. Commits updated `references.bib`
4. Site rebuilds automatically

### Deployment Pipeline

```
push to master
    → GitHub Actions triggers
    → Install Quarto
    → Render site
    → ssh-agent loads passphrase-protected key
    → rsync to SiteGround (port 18765)
```

### Security

- SSH key with passphrase (stored as GitHub secret)
- All secrets in GitHub encrypted storage
- No third-party rsync actions (direct commands)
- Pin GitHub Actions to specific versions
- Dependabot for dependency updates
- SSH known_hosts verification

## GitHub Secrets Required

| Secret | Description |
|--------|-------------|
| `SITEGROUND_HOST` | SSH hostname |
| `SITEGROUND_PORT` | `18765` |
| `SITEGROUND_USER` | SSH username |
| `SITEGROUND_SSH_KEY` | Private key content |
| `SITEGROUND_SSH_PASSPHRASE` | Key passphrase |

## Migration Steps

1. Initialize Quarto project structure
2. Create `_quarto.yml` configuration
3. Migrate content (about, contact, publications, posts)
4. Set up theme and custom styling
5. Create GitHub Actions deploy workflow
6. Set up ORCID publications sync
7. Test local preview
8. Test deployment
9. Clean up old Hugo files

## Design Decisions

- **Quarto over Hugo**: Better multi-language support, native BibTeX/citations, academic-friendly
- **Built-in theme + SCSS**: Low maintenance, full control
- **Direct rsync over actions**: Reduced supply chain risk
- **Passphrase-protected key**: Extra security layer
