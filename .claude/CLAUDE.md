# Stuart Lee Personal Website

## Stack
- Quarto static site generator
- GitHub Actions for CI/CD
- SiteGround hosting (rsync over SSH)

## Commands
- `quarto preview` - Local dev server at localhost:4567
- `quarto render` - Build site to `_site/`
- `git push origin master` - Triggers auto-deploy to SiteGround

## Gotchas
- SCSS must be in theme array, not css field: `theme: [cosmo, styles.scss]`
- SiteGround uses port 18765 for SSH
- SiteGround Dynamic Cache must be flushed after deploys (Site Tools → Speed → Caching)
- GitHub Actions SSH with passphrase keys needs `expect` + `ssh-agent`, not `sshpass`

## Content
- New posts: `quarto create post "title"` in `posts/` directory
- Publications: Edit `references.bib` (auto-synced weekly from ORCID)
- CV: Edit `cv.qmd`
