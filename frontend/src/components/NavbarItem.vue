<script setup lang="ts">
import Icon from "@/components/common/Icon.vue";

const { title, icon, href } = defineProps<{ title: string; icon: string; href: string }>();
</script>

<template>
  <RouterLink
    :to="href"
    class="group flex flex-col items-center justify-center desktop:size-navbar-width desktop:router-link-active:bg-current/5
      mobile:mx-auto mobile:size-navbar-height"
  >
    <Icon :type="icon" class="desktop:text-7 mobile:text-6" />
    <div
      class="text-3/none desktop:mt-0 desktop:h-0 desktop:opacity-0 desktop:transition-all desktop:group-hoctive:mt-2
        desktop:group-hoctive:h-3 desktop:group-hoctive:opacity-100 mobile:mt-1"
      v-text="title"
    ></div>
  </RouterLink>
</template>
