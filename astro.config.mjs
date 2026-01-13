import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
    site: 'https://mrhomeassist.com.au',
    integrations: [tailwind(), sitemap()],
    server: {
        host: true
    },
    preview: {
        host: true
    },
    vite: {
        server: {
            allowedHosts: ['mrhomeassist.com.au', 'www.mrhomeassist.com.au', 'bokk8sowsccckgssoo4s80go.170.64.136.227.sslip.io']
        },
        preview: {
            allowedHosts: ['mrhomeassist.com.au', 'www.mrhomeassist.com.au', 'bokk8sowsccckgssoo4s80go.170.64.136.227.sslip.io']
        }
    }
});