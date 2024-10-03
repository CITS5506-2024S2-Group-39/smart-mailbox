<script setup lang="ts">
import { setIntervalWithCancel } from "@/utils/timeout";
import { shallowRef, watch } from "vue";

const { value } = defineProps<{ value: number }>();
const display = shallowRef<number>(value);
let cancel = () => {};

watch(
  () => value,
  (to: number) => {
    // Cancel previous animation if it is still running
    cancel();

    const from = display.value;
    const diff = to - from;
    const distance = Math.abs(diff);
    if (!distance) {
      // Already there
      return;
    }

    // 15 Frames in 500ms === 30 FPS
    const duration = 500;
    const max = 15;

    const frames = Math.min(distance, max);
    const interval = duration / frames;
    const delta = diff / frames;

    // Current frame of animation
    let current = 0;

    const animate = () => {
      if (++current < frames) {
        // Transition
        display.value += delta;
      } else {
        // End Animation
        display.value = to;
        cancel();
      }
    };

    // Start animation
    cancel = setIntervalWithCancel(animate, interval);
  },
);
</script>

<template>
  <span v-text="Math.round(display) /* Can be decimal during transition, so use Math.round() */"></span>
</template>
