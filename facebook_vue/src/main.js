// Page [ facebook/facebook_vue/src/main.js ]

// main.js
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

// Prime Vue 
import PrimeVue from "primevue/config";
// Popup
import ConfirmationService from 'primevue/confirmationservice'
import DialogService from 'primevue/dialogservice'
// Button
import Button from 'primevue/button';
// Form
import Fluid from 'primevue/fluid';
import InputText from 'primevue/inputtext';
import Password from 'primevue/password';
import FloatLabel from 'primevue/floatlabel';
import Checkbox from 'primevue/checkbox';
import DatePicker from 'primevue/datepicker';
import InputGroup from 'primevue/inputgroup';
import InputGroupAddon from 'primevue/inputgroupaddon';
// Menu
import Menubar from 'primevue/menubar';
import TieredMenu from 'primevue/tieredmenu';
// Image
import Avatar from 'primevue/avatar';
import AvatarGroup from 'primevue/avatargroup';
// Popup
import Popover from 'primevue/popover';
import Dialog from 'primevue/dialog';
// Card
import Card from 'primevue/card';
// Theme
import Noir from './presets/Noir.js';
import ThemeSwitcher from './components/Theme/ThemeSwitcher.vue';
// Toast
import Toast from 'primevue/toast';
import ToastService from 'primevue/toastservice';
// Message
import Message from 'primevue/message';
// PrimeIcons أيقونات 
import 'primeicons/primeicons.css'
import 'tailwindcss/tailwind.css'


const app = createApp(App)

app.use(createPinia())

// مع روابط الصفحات Axios استخدم  
app.use(router, axios)

// eslint-disable-next-line vue/multi-word-component-names
app.component("fa", FontAwesomeIcon)


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
app.use(ConfirmationService);
app.use(DialogService);
// Prime Theme Switcher
app.component('ThemeSwitcher', ThemeSwitcher);
// Prime Button
app.component('prime_button', Button);
// Prime Form
app.component('prime_fluid', Fluid);
app.component('prime_input_text', InputText);
app.component('prime_input_password', Password);
app.component('prime_float_label', FloatLabel);
app.component('prime_check_box', Checkbox);
app.component('prime_date_picker', DatePicker);
app.component('prime_input_group', InputGroup);
app.component('prime_input_group_addon', InputGroupAddon);
// Prime Menu
app.component('prime_menubar', Menubar);
app.component('prime_tiered_menu', TieredMenu);
app.component('prime_avatar', Avatar);
app.component('prime_avatar_group', AvatarGroup);
app.component('prime_popover', Popover);
app.component('prime_card', Card);
app.component('prime_dialog', Dialog);
// Toast
// app.use(Toast);
app.component('prime_toast', Toast);
app.use(ToastService);
// Message
// app.use(Message);
app.component('prime_message', Message);
app.mount('#app')



