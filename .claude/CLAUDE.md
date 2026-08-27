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

## Security headers
- Both sites send HSTS, CSP, nosniff, Referrer-Policy and X-Frame-Options from
  `public/.htaccess` (main) and `public-archive/.htaccess` (archive)
- **The CSP is `default-src 'none'` — the sites load zero JavaScript and zero third-party
  resources.** Adding an external script/font/image, an inline `<script>`, or (on the main
  site) an inline `<style>` will be blocked by the browser and silently break the page.
  Update the relevant `.htaccess` in the same commit, and check devtools for CSP violations.
- `build.inlineStylesheets: "never"` in both configs is load-bearing: with Astro's default
  `'auto'`, a stylesheet under ~4kB gets inlined, which `style-src 'self'` would block
- The archive's CSP allows `'unsafe-inline'` for styles only because Shiki emits inline
  `style=""` attributes on highlighted code
- HSTS is 180 days, per-host, no `includeSubDomains`/`preload` — a new subdomain won't be
  affected, but it must serve HTTPS before you link to it
- HTTPS enforcement is a SiteGround server-level setting, not in `.htaccess`; it survives
  `rsync --delete` (verified)

## Gotchas
- SiteGround uses port 18765 for SSH
- SiteGround Dynamic Cache is auto-flushed after deploys via curl PURGE in the workflow (both hosts)
- GitHub Actions SSH with passphrase keys needs `expect` + `ssh-agent`, not `sshpass`
- Archive docroot path is set in `deploy.yml` env (`ARCHIVE_DOCROOT`)
- System node is v12 (too old for Astro); Node 22 lives at `~/.local/opt/node-v22.14.0-linux-x64/` and is symlinked into `~/.local/bin`, which precedes `/usr/bin` on PATH
- Astro 7 renders markdown with Sätteri, not remark/rehype. No plugins are used, so output is
  unchanged — but adding a remark/rehype plugin now requires `@astrojs/markdown-remark` and
  `markdown.processor: unified()`
- `compressHTML: true` is set explicitly in both configs; Astro 7's `'jsx'` default collapses
  whitespace between inline elements and would alter spacing around mid-sentence links
