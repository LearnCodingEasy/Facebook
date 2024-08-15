# Facebook
👋 Hello! 🗣️ Design presentation about online Social project named “Faceb ook”.

🎨 Design motivation for an online Facebook project.

💖 Please click like and appreciate.

🙏 Thank you for supporting and appreciating my efforts

## Website Build


### 1 Git Clone Project
```
git clone https://github.com/LearnCodingEasy/Facebook.git
``` 

### 2 Create File [ LICENSE ]
```
LICENSE
``` 

### 3 Create Virtual Environment
```
python -m venv facebook_virtual_environment
```

### 4 Activate Virtual Environment
```
facebook_virtual_environment\Scripts\activate
```

### 5 Install Django
```
pip install django
```

### 6 Install Django Libraries [ 1 - djangorestframework | 2 - djangorestframework-simplejwt | 3 - django-cors-headers | 4 - pillow ]
```
pip install djangorestframework djangorestframework-simplejwt django-cors-headers pillow
```

### 7 Create Django Project
```
django-admin startproject facebook_django
```

### 8 Create Vue Project
```
npm create vue@latest
```

### 9 Choose Vite [ Project name & Select a framework ]
```
√ Project name: ... facebook_vue
√ Add TypeScript? ... No / Yes
√ Add JSX Support? ... No / Yes
√ Add Vue Router for Single Page Application development? ... No / Yes
√ Add Pinia for state management? ... No / Yes
√ Add Vitest for Unit Testing? ... No / Yes
√ Add an End-to-End Testing Solution? » No
√ Add ESLint for code quality? ... No / Yes
√ Add Prettier for code formatting? ... No / Yes
√ Add Vue DevTools 7 extension for debugging? (experimental) ... No / Yes

Scaffolding project in E:\Projects\Facebook\facebook_vue...

Done. Now run:

  cd facebook_vue
  npm install
  npm run format
  npm run dev

```
__________________________________________________
### 10 Go To Project [ Install & Run Dev ]
```
cd facebook_vue
npm install
npm run format
npm run build
npm run dev
```
__________________________________________________
### 11  Install Vue Libraries [ 1 - Tailwind | 2 - PrimeVue | 3 - vueuse | 4 - scss | 5 - Axios | 6 - Font Awesome | 7 - Pwa | 8 - | 9 - |  ]
```
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
npm install primevue primeicons
npm install @primevue/themes

npm install -D sass
npm install axios
npm i --save @fortawesome/fontawesome-svg-core @fortawesome/vue-fontawesome@latest @fortawesome/vue-fontawesome@prerelease @fortawesome/free-solid-svg-icons @fortawesome/free-brands-svg-icons @fortawesome/free-regular-svg-icons
npm install -D vite-plugin-pwa
npm i swiper

npm i unplugin-vue-components -D
npm i @primevue/auto-import-resolver -D

```
__________________________________________________
### 12 Configure Tailwind
* tailwind.config.js
```js
content: [
"./index.html",
"./src/**/*.{vue,js,ts,jsx,tsx}",
],
```
* style.css
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### 13 Import Font Awesome
```js
// Font Awesome
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";
// Add Free Icons Styles To SVG Core
library.add(fas, far, fab);

app.component("fa", FontAwesomeIcon)
```

__________________________________________________
### 15 Add Pwa To Vue 
*  
```js
// vite.config.js
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
// For Pwa
// https://vite-pwa-org.netlify.app/guide/
import { VitePWA } from 'vite-plugin-pwa'

export default defineConfig({
  plugins: [
    vue(),
    // For Pwa
    VitePWA({ 
      registerType: 'autoUpdate',
      workbox: {
        globPatterns: ['**/*.{js,css,html,ico,png,svg}'],
        clientsClaim: true,
        skipWaiting: true,
        cleanupOutdatedCaches: false,
        offlineGoogleAnalytics: true,
        sourcemap: true,
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
                maxAgeSeconds: 60 * 60 * 24 * 30 
              }
            }
          }
        ],
      },
      devOptions: {
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
  ]
});

```
__________________________________________________
### 16 Setup Axios
```js
// Axios
// axios استيراد
import axios from "axios"
axios.defaults.baseURL = "http://127.0.0.1:8000"

app.use(router, axios)
```
__________________________________________________
### 17 Setup PrimeVue
```js
// main.js
// Prime Vue 
import PrimeVue from "primevue/config";
// Toast
import ToastService from 'primevue/toastservice';
// Popup
import ConfirmationService from 'primevue/confirmationservice'
import DialogService from 'primevue/dialogservice'
// Element
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import Password from 'primevue/password';
import FloatLabel from 'primevue/floatlabel';
// PrimeIcons أيقونات 
import 'primeicons/primeicons.css'
import 'tailwindcss/tailwind.css'
// Theme
import Noir from './presets/Noir.js';
// Prime Vue 
app.use(PrimeVue, {
  theme: {
      preset: Noir,
      options: {
          prefix: 'p',
          darkModeSelector: '.p-dark',
          cssLayer: false,
      }
  }
});
app.use(ToastService);
app.use(ConfirmationService);
app.use(DialogService);
app.component('prime_button', Button);
app.component('prime_input_text', InputText);
app.component('prime_input_password', Password);
app.component('prime_float_label', FloatLabel);
```
__________________________________________________
### 14 Vue Theme
```html

```
```js

```
__________________________________________________

### 17 Setup Djang Libraries
```python
from datetime import timedelta

WEBSITE_URL = "http://127.0.0.1:8000"

SIMPLE_JWT = {
  "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
  "REFRESH_TOKEN_LIFETIME": timedelta(days=180),
  "ROTATE_REFRESH_TOKENS": False,
}

REST_FRAMEWORK = {
  "DEFAULT_AUTHENTICATION_CLASSES": (
      "rest_framework_simplejwt.authentication.JWTAuthentication",
  ),
  "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:5174",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:5174",
]

INSTALLED_APPS = [
    # ...
    # Libraries
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
]
MIDDLEWARE = [
    # ...
    "corsheaders.middleware.CorsMiddleware",
    # ...
]
```

### 18 Create App [ Account And Setup It ]
``` python
python manage.py startapp account
```
```pyhone
# Page [ account/models.py ]
```
```pyhone
# Page [ account/serializers.py ]
```
```pyhone
# Page [ account/forms.py ]
```
```pyhone
# Page [ account/api.py ]
```
```pyhone
# Page [ account/urls.py ]
```

### 
### 
### 
### 
### 
### 

### 1 Create Page Sign Up
```
```