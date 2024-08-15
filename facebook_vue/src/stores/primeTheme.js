import { reactive } from 'vue';
// import { ref, computed } from 'vue'
// import { defineStore } from 'pinia'
export default {
    install: (app) => {
        const _appState = reactive({ theme: 'Aura', darkTheme: false });

        app.config.globalProperties.$appState = _appState;
    }
};
        