# Stuart Lee Personal Website

## Stack
- Astro static site generator, two builds from one repo:
  - Main site (`astro.config.mjs`): `src/` → `dist/` → https://stuartlee.org
  - Archive (`astro.archive.config.mjs`): `src-archive/` → `dist-archive/` → https://archive.stuartlee.org
- GitHub Actions for CI/CD
- Cloudflare hosting: two static-assets-only Workers (`wrangler.jsonc` → `stuartlee-org`,
  `wrangler.archive.jsonc` → `stuartlee-org-archive`), attached as custom domains
- Cloudflare also runs DNS; the domain is still registered at SiteGround (hosting moved off SiteGround 2026-10-17)

## Commands
- `npm run dev` - Main site dev server
- `npm run dev:archive` - Archive dev server
- `npm run build` - Build both sites
- `git push origin master` - Triggers auto-deploy to Cloudflare (`wrangler deploy` for both configs)
- `npx wrangler dev` / `npx wrangler dev -c wrangler.archive.jsonc` - Serve a build locally with
  production headers/redirects (run `npm run build` first; run one at a time)

## Design
- Spartan, text-first, single-page (modeled on hamiltonulmer.com)
- One stylesheet: `shared/global.css` — CSS custom properties, dark mode via `prefers-color-scheme` (no toggle)
- Fonts: Fraunces (headings), Nunito (body) — self-hosted via @fontsource-variable
- Shared layouts in `shared/` (`Base.astro`, `Post.astro`), imported by both srcDirs via relative paths

## Archive
- The 3 old blog posts live at archive.stuartlee.org with original `/posts/<slug>/` URLs
- Post images are served from `public-archive/posts/<slug>/` (not bundled) because bodies use
  relative/raw-HTML image references; markdown-syntax images use absolute `/posts/<slug>/...` paths
- `public/_redirects` 301-redirects stuartlee.org/posts/* to the archive
- Post copy is verbatim from the old Quarto site — don't edit bodies

## Security headers
- Both sites send HSTS, CSP, nosniff, Referrer-Policy and X-Frame-Options from
  `public/_headers` (main) and `public-archive/_headers` (archive)
- **The CSP is `default-src 'none'` — the sites load zero JavaScript and zero third-party
  resources.** Adding an external script/font/image, an inline `<script>`, or (on the main
  site) an inline `<style>` will be blocked by the browser and silently break the page.
  Update the relevant `_headers` in the same commit, and check devtools for CSP violations.
- `build.inlineStylesheets: "never"` in both configs is load-bearing: with Astro's default
  `'auto'`, a stylesheet under ~4kB gets inlined, which `style-src 'self'` would block
- The archive's CSP allows `'unsafe-inline'` for styles only because Shiki emits inline
  `style=""` attributes on highlighted code
- HSTS is 180 days, per-host, no `includeSubDomains`/`preload` — a new subdomain won't be
  affected, but it must serve HTTPS before you link to it
- HTTP→HTTPS is Cloudflare's "Always Use HTTPS" zone setting, not in the repo
- `www.stuartlee.org` is a Cloudflare Redirect Rule (proxied DNS record), not a Worker

## Gotchas
- Wrangler deploys from CI need repo secrets `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`
- `workers_dev` is unset, so the `*.workers.dev` URLs are disabled; the custom domains are the only way in
- No email on the domain (SiteGround mail went with the hosting plan)
- System node is v12 (too old for Astro); Node 22 lives at `~/.local/opt/node-v22.14.0-linux-x64/` and is symlinked into `~/.local/bin`, which precedes `/usr/bin` on PATH
- Astro 7 renders markdown with Sätteri, not remark/rehype. No plugins are used, so output is
  unchanged — but adding a remark/rehype plugin now requires `@astrojs/markdown-remark` and
  `markdown.processor: unified()`
- `compressHTML: true` is set explicitly in both configs; Astro 7's `'jsx'` default collapses
  whitespace between inline elements and would alter spacing around mid-sentence links
