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
- Dark mode uses separate theme file: `dark: [darkly, styles-dark.scss]` (not CSS selectors)
- Gradient text `-webkit-text-fill-color: transparent` bleeds into child elements - scope to specific tags like `h1.hero-title`
- SiteGround uses port 18765 for SSH
- SiteGround Dynamic Cache must be flushed after deploys (Site Tools → Speed → Caching)
- GitHub Actions SSH with passphrase keys needs `expect` + `ssh-agent`, not `sshpass`

## Theming
- Light theme: `styles.scss` (Aurora Editorial - warm whites, coral/peach accents)
- Dark theme: `styles-dark.scss` (warm espresso browns, cream text)
- Fonts: Fraunces (headings), Nunito (body)
- New content directories must be added to `_quarto.yml` render list

## Accessibility
- Focus states: 3px outline with `$aurora-coral` (light) / `$aurora-peach` (dark)
- Reduced motion: `@media (prefers-reduced-motion: reduce)` disables animations
- Touch targets: Buttons have 44px min-height
- High contrast: Gradient text has `@media (forced-colors: active)` fallback

## Content
- New posts: `quarto create post "title"` in `posts/` directory
- Publications: Edit `references.bib` (auto-synced weekly from ORCID)
- CV: Edit `cv.qmd`
- Elsewhere pages: `rooms/` directory (coffee, film, books, notes, internet)
