<script setup lang="ts">
// Handler to emulate click on Enter key
const triggerClick = (e: KeyboardEvent) => {
  const target = e.target as HTMLElement;
  target.click();
};
</script>

<template>
  <div tabindex="0" @keydown.enter.prevent.stop="triggerClick($event)" class="cursor-pointer">
    <slot></slot>
  </div>
</template>

<style>
/* This is an unstyled element emulating the behavior of default <button> */
</style>
