<script setup lang="ts">
import MailboxEventIcon from "@/components/MailboxEventIcon.vue";

import { type MailboxEvent } from "@/types/MailboxEvent";
const { event } = defineProps<{ event: MailboxEvent }>();
</script>

<template>
  <RouterLink
    :to="`/event/${event.id}`"
    class="group flex p-2 gap-2 rounded-lg hover:bg-gray-100 focus-visible:bg-gray-100 active:bg-gray-100"
  >
    <div
      class="flex-none relative group-first-of-type:before:hidden group-last-of-type:after:hidden before:border-l-2 before:absolute
        before:left-[50%] before:-top-2 before:h-2 after:border-l-2 after:absolute after:left-[50%] after:top-12 after:-bottom-2"
    >
      <MailboxEventIcon class="rounded-full border-2 w-12 h-12 p-2 text-7" :type="event.type" />
    </div>
    <div class="flex-1">
      <div class="text-xs text-gray-500" v-text="new Date(event.time).toLocaleString()"></div>
      <div class="font-bold break-all" v-text="event.type"></div>
      <div class="text-sm text-gray-500" v-text="event.comment"></div>
    </div>
  </RouterLink>
</template>
