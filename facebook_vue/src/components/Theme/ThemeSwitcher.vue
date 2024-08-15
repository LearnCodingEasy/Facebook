<template>
  <span class="">
    <ul class="flex list-none m-0 p-0 gap-2 items-center">
      <li>
        <button
          type="button"
          class="inline-flex w-8 h-8 p-0 items-center justify-center surface-0 dark:surface-800 border border-surface-200 dark:border-surface-600 rounded"
          @click="onThemeToggler"
        >
          <i :class="`dark:text-white pi ${iconClass}`" />
        </button>
      </li>
    </ul>
  </span>
</template>

<script>
import { updatePreset, updateSurfacePalette } from '@primevue/themes'

export default {
  data() {
    return {
      iconClass: 'pi-moon',
      selectedPrimaryColor: 'noir',
      selectedSurfaceColor: null,

      surfaces: [
        {
          name: 'slate',
          palette: {
            0: '#ffffff',
            50: '#f8fafc',
            100: '#f1f5f9',
            200: '#e2e8f0',
            300: '#cbd5e1',
            400: '#94a3b8',
            500: '#64748b',
            600: '#475569',
            700: '#334155',
            800: '#1e293b',
            900: '#0f172a',
            950: '#020617'
          }
        },
        {
          name: 'gray',
          palette: {
            0: '#ffffff',
            50: '#f9fafb',
            100: '#f3f4f6',
            200: '#e5e7eb',
            300: '#d1d5db',
            400: '#9ca3af',
            500: '#6b7280',
            600: '#4b5563',
            700: '#374151',
            800: '#1f2937',
            900: '#111827',
            950: '#030712'
          }
        },
        {
          name: 'zinc',
          palette: {
            0: '#ffffff',
            50: '#fafafa',
            100: '#f4f4f5',
            200: '#e4e4e7',
            300: '#d4d4d8',
            400: '#a1a1aa',
            500: '#71717a',
            600: '#52525b',
            700: '#3f3f46',
            800: '#27272a',
            900: '#18181b',
            950: '#09090b'
          }
        },
        {
          name: 'neutral',
          palette: {
            0: '#ffffff',
            50: '#fafafa',
            100: '#f5f5f5',
            200: '#e5e5e5',
            300: '#d4d4d4',
            400: '#a3a3a3',
            500: '#737373',
            600: '#525252',
            700: '#404040',
            800: '#262626',
            900: '#171717',
            950: '#0a0a0a'
          }
        },
        {
          name: 'stone',
          palette: {
            0: '#ffffff',
            50: '#fafaf9',
            100: '#f5f5f4',
            200: '#e7e5e4',
            300: '#d6d3d1',
            400: '#a8a29e',
            500: '#78716c',
            600: '#57534e',
            700: '#44403c',
            800: '#292524',
            900: '#1c1917',
            950: '#0c0a09'
          }
        },
        {
          name: 'soho',
          palette: {
            0: '#ffffff',
            50: '#f4f4f4',
            100: '#e8e9e9',
            200: '#d2d2d4',
            300: '#bbbcbe',
            400: '#a5a5a9',
            500: '#8e8f93',
            600: '#77787d',
            700: '#616268',
            800: '#4a4b52',
            900: '#34343d',
            950: '#1d1e27'
          }
        },
        {
          name: 'viva',
          palette: {
            0: '#ffffff',
            50: '#f3f3f3',
            100: '#e7e7e8',
            200: '#cfd0d0',
            300: '#b7b8b9',
            400: '#9fa1a1',
            500: '#87898a',
            600: '#6e7173',
            700: '#565a5b',
            800: '#3e4244',
            900: '#262b2c',
            950: '#0e1315'
          }
        },
        {
          name: 'ocean',
          palette: {
            0: '#ffffff',
            50: '#fbfcfc',
            100: '#F7F9F8',
            200: '#EFF3F2',
            300: '#DADEDD',
            400: '#B1B7B6',
            500: '#828787',
            600: '#5F7274',
            700: '#415B61',
            800: '#29444E',
            900: '#183240',
            950: '#0c1920'
          }
        }
      ]
    }
  },
  methods: {
    onThemeToggler() {
      const root = document.getElementsByTagName('html')[0]

      root.classList.toggle('p-dark')
      this.iconClass = this.iconClass === 'pi-moon' ? 'pi-sun' : 'pi-moon'
    },

    updateColors(type, color) {
      if (type === 'primary') this.selectedPrimaryColor = color.name
      else if (type === 'surface') this.selectedSurfaceColor = color.name

      this.applyTheme(type, color)
    },
    applyTheme(type, color) {
      if (type === 'primary') {
        updatePreset(this.getPresetExt())
      } else if (type === 'surface') {
        updateSurfacePalette(color.palette)
      }
    },
    onRippleChange(value) {
      this.$primevue.config.ripple = value
    }
  },
  computed: {
    rippleActive() {
      return this.$primevue.config.ripple
    }
  }
}
</script>
