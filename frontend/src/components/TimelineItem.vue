<script setup lang="ts">
import MailboxEventIcon from "@/components/MailboxEventIcon.vue";
import { type MailboxEvent } from "@/stores/events";
import { computed } from "vue";

const { event } = defineProps<{ event: MailboxEvent }>();
const date = computed(() => event.time as Date);
</script>

<template>
  <div class="group flex flex-row gap-std px-std py-std/2 transition-colors last-of-type:pb-std hoctive:bg-current/5">
    <div class="w-28 text-right text-xs/loose text-neutral-500 mobile:hidden">
      <div v-text="date.toLocaleDateString()"></div>
      <div v-text="date.toLocaleTimeString()"></div>
    </div>
    <div class="-my-std/2 flex flex-col items-center">
      <!-- The upper line -->
      <div class="h-std/2 w-[2px] bg-neutral-200 group-first-of-type:invisible"></div>
      <!-- The center circle -->
      <div class="grid place-items-center rounded-full border-[2px] border-neutral-200 desktop:size-13 mobile:size-12">
        <MailboxEventIcon class="desktop:text-8 mobile:text-7" :type="event.type" />
      </div>
      <!-- The lower line -->
      <div class="w-[2px] flex-1 bg-neutral-200 group-last-of-type:invisible"></div>
    </div>
    <div class="flex flex-1 flex-col gap-1">
      <div class="text-xs text-neutral-500 desktop:hidden" v-text="date.toLocaleString()"></div>
      <RouterLink :to="`/event/${event.id}`" class="block break-all text-base font-bold">{{ event.type }}</RouterLink>
      <div class="text-sm text-neutral-500" v-text="event.data.summary"></div>
    </div>
  </div>
</template>
