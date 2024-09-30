<script setup lang="ts">
import MaterialIcon from "@/components/MaterialIcon.vue";

const { title, icon, href } = defineProps<{ title: string; icon: string; href: string }>();
</script>

<template>
  <RouterLink
    :to="href"
    class="flex flex-none flex-col items-center justify-center desktop:size-navbar-width desktop:gap-2 desktop:transition-colors
      desktop:hoctive:bg-current/5 mobile:mx-auto mobile:size-navbar-height mobile:gap-1"
  >
    <MaterialIcon :type="icon" class="desktop:text-7 mobile:text-6" />
    <div class="select-none text-xs/none" v-text="title"></div>
  </RouterLink>
</template>
