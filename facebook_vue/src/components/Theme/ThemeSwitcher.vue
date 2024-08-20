<template>
  <span class="">
    <ul class="flex list-none m-0 p-0 gap-2 items-center">
      <li>
        <button
          type="button"
          class="inline-flex w-8 h-8 p-0 items-center justify-center surface-0 dark:surface-800 border border-surface-200 dark:border-surface-600 rounded-full"
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
      selectedSurfaceColor: null
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
