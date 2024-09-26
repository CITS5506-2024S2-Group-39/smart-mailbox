<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header>
    <!-- To be added -->
  </header>
  <main class="p-4 sm:p-0 sm:max-w-md md:max-w-lg lg:max-w-xl xl:max-w-2xl mx-auto">
    <RouterView />
  </main>
</template>

<style>
@tailwind base;
@tailwind components;
@tailwind utilities;
</style>
