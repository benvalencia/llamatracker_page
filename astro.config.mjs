import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind";
const LIVE_URL = 'https://www.llamatracker.net';

// https://astro.build/config
export default defineConfig({
  site: LIVE_URL,
  base: '/',
  integrations: [tailwind()],
  i18n: {
    defaultLocale: 'en',
    locales: ['es', 'en', 'it', 'ca'],
    routing: {
      prefixDefaultLocale: false
    }
  }
});