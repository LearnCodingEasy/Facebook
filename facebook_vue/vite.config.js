import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// For Pwa
// https://vite-pwa-org.netlify.app/guide/
import { VitePWA } from 'vite-plugin-pwa'
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    // For Pwa
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['favicon.ico', 'robots.txt', 'apple-touch-icon.png'],
      manifest: {
        name: 'Tom And Jerry',
        short_name: 'T&J',
        description: 'Tom And Jerry PWA Application',
        theme_color: '#ffffff',
        icons: [
          {
            "src": "./public/images/icons/icon-72x72.png",
            "type": "image/png",
            "sizes": "72x72",
            "purpose": "any maskable"
          },
          {
            "src": "./public/images/icons/icon-96x96.png",
            "type": "image/png",
            "sizes": "96x96",
            "purpose": "any maskable"
          },
          {
            "src": "./public/images/icons/icon-128x128.png",
            "type": "image/png",
            "sizes": "128x128",
            "purpose": "any maskable"
          },
          {
            "src": "./public/images/icons/icon-144x144.png",
            "type": "image/png",
            "sizes": "144x144",
            "purpose": "any maskable"
          },
          {
            "src": "./public/images/icons/icon-152x152.png",
            "type": "image/png",
            "sizes": "152x152",
            "purpose": "any maskable"
          },
          {
            "src": "./public/images/icons/icon-192x192.png",
            "type": "image/png",
            "sizes": "192x192",
            "purpose": "any maskable"
          },
          {
            "src": "./public/images/icons/icon-384x384.png",
            "type": "image/png",
            "sizes": "384x384",
            "purpose": "any maskable"
          },
          {
            "src": "./public/images/icons/icon-512x512.png",
            "type": "image/png",
            "sizes": "512x512",
            "purpose": "any maskable"
          }
        ],
        screenshots: [
          {
            "src": "./images/screenshots/screenshots.png",
            "sizes": "640x480",
            "type": "image/png",
            "form_factor": "wide"
            // "form_factor": "narrow"
          }
        ]
      },
      workbox: {
        runtimeCaching: [
          {
            urlPattern: ({ request }) => 
              request.destination === 'document' || 
              request.destination === 'script' || 
              request.destination === 'style' || 
              request.destination === 'image' || 
              request.destination === 'font',
            handler: 'StaleWhileRevalidate',
            options: {
              cacheName: 'assets-cache',
              expiration: {
                maxEntries: 100,
                maxAgeSeconds: 60 * 60 * 24 * 30 // 30 days
              }
            }
          }
        ],
        offlineGoogleAnalytics: true,
        skipWaiting: true,
        clientsClaim: true
      }
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
