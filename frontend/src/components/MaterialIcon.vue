<script setup lang="ts">
const { type } = defineProps<{ type: string }>();
</script>

<template>
  <span class="font-icon" v-text="type"></span>
</template>

<style>
@font-face {
  /* https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200 */
  font-family: "Material Symbols Outlined";
  src: url(https://fonts.gstatic.com/s/materialsymbolsoutlined/v207/kJEhBvYX7BgnkSrUwT8OhrdQw4oELdPIeeII9v6oFsI.woff2)
    format("woff2");
  font-display: block;
}
.font-icon {
  /* Please set font size outside */
  @apply select-none leading-none;
  font-family: "Material Symbols Outlined";
}
/* Use filled icon for active <RouterLink> */
.router-link-active .font-icon {
  font-variation-settings: "FILL" 1;
}
</style>
