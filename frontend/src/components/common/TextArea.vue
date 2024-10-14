<script setup lang="ts">
import { onMounted, shallowRef, watch } from "vue";

const model = defineModel<string>({ required: true });
const input = shallowRef<HTMLTextAreaElement>();

onMounted(() => {
  const element = input.value as HTMLTextAreaElement;
  watch(
    model,
    () => {
      // automatically adjust height based on content
      element.style.height = "0";
      element.style.height = element.scrollHeight + "px";
    },
    { immediate: true },
  );
});
</script>

<template>
  <textarea ref="input" v-model="model"></textarea>
</template>
