import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://archive.stuartlee.org",
  srcDir: "src-archive",
  publicDir: "public-archive",
  outDir: "dist-archive",
  markdown: {
    shikiConfig: {
      themes: { light: "github-light", dark: "github-dark" },
    },
  },
});
