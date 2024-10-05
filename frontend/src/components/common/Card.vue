<script setup lang="ts">
const { title } = defineProps<{ title?: string }>();
</script>

<template>
  <div class="flex flex-col gap-std overflow-auto rounded-lg border border-neutral-200 bg-white p-std">
    <div class="flex flex-row items-center" v-if="title">
      <div class="text-base font-bold" v-text="title"></div>
      <div class="flex-1"></div>
      <slot name="additional"></slot>
    </div>
    <slot></slot>
  </div>
</template>
