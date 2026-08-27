import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://stuartlee.org",
  srcDir: "src",
  publicDir: "public",
  outDir: "dist",
  build: {
    // Keep stylesheets external so the CSP can stay on style-src 'self'.
    // With the default 'auto', a small enough stylesheet gets inlined and
    // would be blocked, leaving the page unstyled.
    inlineStylesheets: "never",
  },
});
