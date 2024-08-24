// Page [ facebook/facebook_vue/vite.config.js ]

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
      // ليكون "تحديث تلقائي" Service Worker إعداد نوع التسجيل لـ 
      registerType: 'autoUpdate',
      workbox: {
        // Service Worker أنماط الملفات التي سيتم تخزينها مسبقًا في الـ 
        globPatterns: ['**/*.{js,css,html,ico,png,svg}'],
        // يتحكم في كل العملاء الحاليين دون الحاجة لإعادة التحميل Service Worker يجعل الـ 
        clientsClaim: true,
         //  Service Worker يتجاوز فترة الانتظار وينشط الـ 
        skipWaiting: true,
        // ولا يُنظفها Cache يُبقي على النسخ القديمة من الـ 
        cleanupOutdatedCaches: false,
        // للعمل أثناء عدم الاتصال بالإنترنت Google يتيح تحليلات 
        offlineGoogleAnalytics: true,
        // (الخرائط المصدرية) لتسهيل تتبع الأخطاء sourcemaps تفعيل 
        sourcemap: true,
        runtimeCaching: [
          {
            // أو نوع الطلبات التي سيتم تخزينها أثناء التشغيل URL تحديد نمط 
            urlPattern: ({ request }) => 
              request.destination === 'document' || 
              request.destination === 'script' || 
              request.destination === 'style' || 
              request.destination === 'image' || 
              request.destination === 'font',
            // استراتيجية التخزين المؤقت التي تعرض النسخة المخزنة مؤقتًا أثناء الحصول على نسخة جديدة من الشبكة
            handler: 'StaleWhileRevalidate',
            options: {
              // المستخدم لتخزين هذه الملفات (cache) اسم الكاش 
              cacheName: 'assets-cache',
              expiration: {
                // عدد الملفات التي يمكن تخزينها في الكاش كحد أقصى
                maxEntries: 100,
                // مدة التخزين المؤقت لهذه الملفات (30 يومًا)
                maxAgeSeconds: 60 * 60 * 24 * 30 
              }
            }
          }
        ],
      },
      devOptions: {
         // PWA تمكين خيارات التطوير أثناء تطوير 
        enabled: true
      },
      injectRegister: 'auto',
      includeAssets: ["**/*"],
      manifest: {
        name: 'Facebook',
        short_name: 'Facebook',
        description: 'My Awesome App Facebook',
        theme_color: '#ffffff',
        icons: [
                {
                  "src": "./images/icons/facebook_icon_72x72.png",
                  "type": "image/png",
                  "sizes": "72x72",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_96x96.png",
                  "type": "image/png",
                  "sizes": "96x96",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_128x128.png",
                  "type": "image/png",
                  "sizes": "128x128",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_144x144.png",
                  "type": "image/png",
                  "sizes": "144x144",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_152x152.png",
                  "type": "image/png",
                  "sizes": "152x152",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_192x192.png",
                  "type": "image/png",
                  "sizes": "192x192",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_384x384.png",
                  "type": "image/png",
                  "sizes": "384x384",
                  "purpose": "any maskable"
                },
                {
                  "src": "./images/icons/facebook_icon_512x512.png",
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
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
