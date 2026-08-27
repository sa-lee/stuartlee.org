import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://archive.stuartlee.org",
  compressHTML: true,
  srcDir: "src-archive",
  publicDir: "public-archive",
  outDir: "dist-archive",
  build: {
    inlineStylesheets: "never",
  },
  markdown: {
    shikiConfig: {
      themes: { light: "github-light", dark: "github-dark" },
    },
  },
});
