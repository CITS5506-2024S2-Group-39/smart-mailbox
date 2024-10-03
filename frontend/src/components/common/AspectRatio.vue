<script setup lang="ts">
const { ratio } = defineProps<{ ratio: string | number }>();
</script>

<template>
  <div class="relative">
    <svg class="w-full" :style="{ aspectRatio: ratio }"></svg>
    <div class="absolute inset-0">
      <slot></slot>
    </div>
  </div>
</template>
