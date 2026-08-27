# Stuart Lee Personal Website

## Stack
- Astro static site generator, two builds from one repo:
  - Main site (`astro.config.mjs`): `src/` → `dist/` → https://stuartlee.org
  - Archive (`astro.archive.config.mjs`): `src-archive/` → `dist-archive/` → https://archive.stuartlee.org
- GitHub Actions for CI/CD
- SiteGround hosting (rsync over SSH)

## Commands
- `npm run dev` - Main site dev server
- `npm run dev:archive` - Archive dev server
- `npm run build` - Build both sites
- `git push origin master` - Triggers auto-deploy to SiteGround

## Design
- Spartan, text-first, single-page (modeled on hamiltonulmer.com)
- One stylesheet: `shared/global.css` — CSS custom properties, dark mode via `prefers-color-scheme` (no toggle)
- Fonts: Fraunces (headings), Nunito (body) — self-hosted via @fontsource-variable
- Shared layouts in `shared/` (`Base.astro`, `Post.astro`), imported by both srcDirs via relative paths

## Archive
- The 3 old blog posts live at archive.stuartlee.org with original `/posts/<slug>/` URLs
- Post images are served from `public-archive/posts/<slug>/` (not bundled) because bodies use
  relative/raw-HTML image references; markdown-syntax images use absolute `/posts/<slug>/...` paths
- `public/.htaccess` 301-redirects stuartlee.org/posts/* to the archive
- Post copy is verbatim from the old Quarto site — don't edit bodies

## Gotchas
- SiteGround uses port 18765 for SSH
- SiteGround Dynamic Cache is auto-flushed after deploys via curl PURGE in the workflow (both hosts)
- GitHub Actions SSH with passphrase keys needs `expect` + `ssh-agent`, not `sshpass`
- Archive docroot path is set in `deploy.yml` env (`ARCHIVE_DOCROOT`)
- System node is v12 (too old for Astro); Node 22 lives at `~/.local/opt/node-v22.14.0-linux-x64/` and is symlinked into `~/.local/bin`, which precedes `/usr/bin` on PATH
