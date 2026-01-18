import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
    site: 'https://www.localrankadvantage.shop',
    integrations: [tailwind() /*, sitemap() */],
    server: {
        host: true
    },
    preview: {
        host: true
    },
    vite: {
        server: {
            allowedHosts: ['localrankadvantage.shop', 'www.localrankadvantage.shop', 'bokk8sowsccckgssoo4s80go.170.64.136.227.sslip.io']
        },
        preview: {
            allowedHosts: ['localrankadvantage.shop', 'www.localrankadvantage.shop', 'bokk8sowsccckgssoo4s80go.170.64.136.227.sslip.io']
        }
    }
});