import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
    site: 'https://www.example.com',
    integrations: [tailwind() /*, sitemap() */],
    server: {
        host: true
    },
    preview: {
        host: true
    },
    vite: {
        server: {
            allowedHosts: ['localhost', '.sslip.io']
        }
    }
});