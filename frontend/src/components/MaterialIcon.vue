<script setup lang="ts">
const { type } = defineProps<{ type: string }>();
</script>

<template>
  <div class="material-icon" v-text="type"></div>
</template>

<style>
/* Modified version of https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0 */

@font-face {
  font-family: "Material Symbols Outlined";
  font-style: normal;
  font-weight: 400;
  src: url(https://fonts.gstatic.com/s/materialsymbolsoutlined/v207/kJF1BvYX7BgnkSrUwT8OhrdQw4oELdPIeeII9v6oDMzByHX9rA6RzaxHMPdY43zj-jCxv3fzvRNU22ZXGJpEpjC_1v-p_4MrImHCIJIZrDCvHOej.woff2)
    format("woff2");
}

.material-icon {
  font-family: "Material Symbols Outlined";
  font-weight: normal;
  font-style: normal;
  line-height: 1;
  letter-spacing: normal;
  text-transform: none;
  white-space: nowrap;
  word-wrap: normal;
  direction: ltr;
  user-select: none;
}
</style>
