<script setup lang="ts">
const { title } = defineProps<{ title?: string }>();
</script>

<template>
  <div class="flex flex-col desktop:gap-8 desktop:border desktop:px-12 desktop:py-8 mobile:gap-4">
    <div class="flex flex-none flex-row items-center" v-if="title">
      <div class="flex-none text-base font-bold" v-text="title"></div>
      <div class="flex-1"></div>
      <div class="flex-none">
        <slot name="additional"></slot>
      </div>
    </div>
    <slot></slot>
  </div>
</template>
