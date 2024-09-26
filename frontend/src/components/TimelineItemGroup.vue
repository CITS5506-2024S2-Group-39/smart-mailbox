<script setup lang="ts">
import MaterialIcon from "@/components/MaterialIcon.vue";
import TimelineItem from "@/components/TimelineItem.vue";

import { type MailboxEvent } from "@/types/MailboxEvent";
const { title, events } = defineProps<{
  title: string;
  events: MailboxEvent[];
}>();

import { ref } from "vue";
const collapsed = ref<boolean>(false);
</script>

<template>
  <div>
    <a
      class="p-2 flex gap-2 items-center rounded-lg transition-colors hover:bg-gray-100 focus-visible:bg-gray-100 active:bg-gray-100"
      href="javascript:;"
      @click="collapsed = !collapsed"
    >
      <MaterialIcon
        class="text-gray-500 transition-all"
        type="keyboard_arrow_down"
        :class="{ '-rotate-90': collapsed }"
      />
      <span class="font-bold" v-text="title"></span>
    </a>
    <Transition v-show="!collapsed">
      <div class="transition-height">
        <TimelineItem v-for="event of events" :key="event.id" :event="event" />
      </div>
    </Transition>
  </div>
</template>

<style>
.transition-height.v-enter-from,
.transition-height.v-leave-to {
  max-height: 0;
  opacity: 0;
}
.transition-height.v-enter-to,
.transition-height.v-leave-from {
  opacity: 1;
  max-height: 100vh;
}
.transition-height.v-enter-active,
.transition-height.v-leave-active {
  @apply transition-all;
}
</style>
