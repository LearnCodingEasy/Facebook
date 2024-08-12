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

// Axios
// axios استيراد
import axios from "axios"
// Backend للاتصال مع ال URL افتراضية لجميع طلبات axios تعيين قاعدة
axios.defaults.baseURL = "http://127.0.0.1:8000"

const app = createApp(App)

app.use(createPinia())

// مع روابط الصفحات Axios استخدم  
app.use(router, axios)

// eslint-disable-next-line vue/multi-word-component-names
app.component("fa", FontAwesomeIcon)
app.mount('#app')



