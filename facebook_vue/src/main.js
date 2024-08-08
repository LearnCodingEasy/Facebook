// Tailwind
import './assets/main.css'
import './assets/Scss/Style.scss'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

// Font Awesome
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";
// Add Free Icons Styles To SVG Core
library.add(fas, far, fab);

const app = createApp(App)

app.use(createPinia())
app.use(router)
// eslint-disable-next-line vue/multi-word-component-names
app.component("fa", FontAwesomeIcon)
app.mount('#app')


// For Pwa
// Register Service Worker
// if ('serviceWorker' in navigator) {
//   window.addEventListener('load', () => {
//     navigator.serviceWorker.register('/sw.js')
//       .then(registration => {
//         console.log('Service Worker registered with scope:', registration.scope);
//       })
//       .catch(error => {
//         console.error('Service Worker registration failed:', error);
//         console.error('Service Worker registration failed:', error.message);
//       });
//   });
// }