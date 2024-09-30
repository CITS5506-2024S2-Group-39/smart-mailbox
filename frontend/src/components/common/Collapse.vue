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
  opacity: 0;
  max-height: 0;
}
.collapse-enter-to,
.collapse-leave-from {
  opacity: 1;
  max-height: 100vh;
}
.collapse-enter-active,
.collapse-leave-active {
  @apply transition-all;
}
</style>
