<script setup lang="ts">
const { collapsed } = defineProps<{ collapsed: boolean }>();
</script>

<template>
  <Transition name="collapse">
    <div v-show="!collapsed">
      <slot></slot>
    </div>
  </Transition>
</template>

<style>
.collapse-enter-from,
.collapse-leave-to {
  @apply opacity-0;
  @apply max-h-0;
}
.collapse-enter-to,
.collapse-leave-from {
  @apply opacity-100;
  @apply max-h-screen;
}
.collapse-enter-active,
.collapse-leave-active {
  @apply transition-all !important;
}
</style>
