<script setup lang="ts">
import MailboxEventIcon from "@/components/MailboxEventIcon.vue";
import { type MailboxEvent } from "@/types/MailboxEvent";
import { computed } from "vue";

const { event } = defineProps<{ event: MailboxEvent }>();
const date = computed(() => event.time as Date);
</script>

<template>
  <div
    class="group flex flex-row desktop:gap-8 desktop:p-4 desktop:transition-all desktop:hoctive:bg-current/5 mobile:gap-4
      mobile:py-2"
  >
    <div class="mt-1 min-w-24 flex-none text-right text-xs text-gray-500 mobile:hidden">
      <div v-text="date.toLocaleDateString()"></div>
      <div v-text="date.toLocaleTimeString()"></div>
    </div>
    <div
      class="relative flex-none after:absolute after:left-[50%] after:top-12 after:border-l-2 group-first-of-type:before:hidden
        group-last-of-type:after:hidden desktop:after:-bottom-8 mobile:after:-bottom-4"
    >
      <div class="grid size-12 place-items-center rounded-full border-2">
        <MailboxEventIcon class="text-8" :type="event.type" />
      </div>
    </div>
    <div class="flex-1">
      <div class="mb-1 text-xs text-gray-500 desktop:hidden" v-text="date.toLocaleString()"></div>
      <RouterLink :to="`/event/${event.id}`" class="mb-1 block break-all text-base font-bold" v-text="event.type" />
      <div class="text-sm text-gray-500" v-text="event.comment"></div>
    </div>
  </div>
</template>
