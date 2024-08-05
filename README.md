# Facebook

# 1 Git Clone Project
```
git clone https://github.com/LearnCodingEasy/Facebook.git
``` 

# 2 Create File [ LICENSE ]
```
LICENSE
``` 

# 3 Create Virtual Environment
```
python -m venv facebook_virtual_environment
```

# 4 Activate Virtual Environment
```
facebook_virtual_environment\Scripts\activate
```

# 5 Install Django
```
pip install django
```

# 6 Install Django Libraries [ 1 - djangorestframework | 2 - djangorestframework-simplejwt | 3 - django-cors-headers | 4 - pillow ]
```
pip install djangorestframework djangorestframework-simplejwt django-cors-headers pillow
```

# 7 Create Django Project
```
django-admin startproject facebook_django
```

# 8 Create Vue Project
```
npm create vue@latest
```

# 9 Choose Vite [ Project name & Select a framework ]
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

# 10 Go To Project [ Install & Run Dev ]
```
cd facebook_vue
npm install
npm run format
npm run dev
```

# 11  Install Vue Libraries [ 1 - Tailwind | 2 - PrimeVue | 3 - vueuse | 4 - scss | 5 - Axios | 6 - Font Awesome | 7 - | 8 - | 9 - |  ]
```
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
npm install primevue primeicons
npm i @vueuse/core
npm install -D sass
npm install axios
npm i --save @fortawesome/fontawesome-svg-core @fortawesome/vue-fontawesome@latest @fortawesome/vue-fontawesome@prerelease @fortawesome/free-solid-svg-icons @fortawesome/free-brands-svg-icons @fortawesome/free-regular-svg-icons

npm i unplugin-vue-components -D
npm i @primevue/auto-import-resolver -D

```

# 12 Configure Tailwind
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

# 13 Import Font Awesome
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
```css
// Global Color Light Theme
:root {
  /* Body */
  --body-bg: #f0f2f5;
}

// Style For Dark Mode
html.dark {
  --body-bg: #0d121b;
}
body {
  background-color: var(--body-bg);
}
```
# 14 Vue Theme
```html
<!-- Icon Change Theme -->
<button @click="toggleDarkMode()" class="wrapper-change-theme">
  <fa class="change-theme" :icon="currentIcon"></fa>
</button>
```
```js
<script setup>
import { useDark } from '@vueuse/core'
import { useToggle } from '@vueuse/core'
import { ref } from 'vue'

let isDark = useDark()
let toggleDark = useToggle(isDark)

// الحالة لتتبع الأيقونة الحالية
const currentIcon = ref(['fas', 'moon'])

// دالة تبديل الأيقونة عند الضغط على الزر
const toggleDarkMode = () => {
  toggleDark()
  currentIcon.value = isDark.value ? ['fas', 'sun'] : ['fas', 'moon']
}
</script>
```

# 14 
* 
```
```
