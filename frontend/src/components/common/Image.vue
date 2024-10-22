<script setup lang="ts">
import { shallowRef } from "vue";

const { src } = defineProps<{ src: string }>();
const zoom = shallowRef<boolean>(false);

const toggleZoom = (zoomed: boolean) => {
  if (!zoomed) document.body.style.overflow = "";
  else document.body.style.overflow = "hidden";
  zoom.value = zoomed;
};
</script>

<template>
  <div>
    <img :src class="rounded-lg" @click="toggleZoom(true)" />

    <div v-if="zoom" @click="toggleZoom(false)" class="fixed inset-0 z-50 grid place-items-center bg-neutral-950/75">
      <img :src />
    </div>
  </div>
</template>
