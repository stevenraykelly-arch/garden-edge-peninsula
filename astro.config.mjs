import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
    site: 'https://landscaperspakenham.com.au',
    integrations: [tailwind() /*, sitemap() */],
    server: {
        host: true
    },
    preview: {
        host: true
    },
    vite: {
        server: {
            allowedHosts: ['landscaperspakenham.com.au', 'www.landscaperspakenham.com.au', 'w4cw84cwkwskc0cw4c80gs8k.170.64.136.227.sslip.io']
        },
        preview: {
            allowedHosts: ['landscaperspakenham.com.au', 'www.landscaperspakenham.com.au', 'w4cw84cwkwskc0cw4c80gs8k.170.64.136.227.sslip.io']
        }
    }
});