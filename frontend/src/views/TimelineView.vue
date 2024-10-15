<script setup lang="ts">
import List from "@/components/common/List.vue";
import TimelineItemGroup from "@/components/TimelineItemGroup.vue";
import events, { type MailboxEvent } from "@/stores/events";
import { computed } from "vue";

// Mailbox events grouped by date
const groups = computed(() => {
  const map: Record<string, MailboxEvent[]> = {};
  for (const event of events) {
    const datetime = event.time as Date;
    const key = datetime.toLocaleDateString();
    let group = map[key];
    if (!group) {
      group = [];
      map[key] = group;
    }
    group.push(event);
  }
  return map;
});
</script>

<template>
  <List class="flex flex-col gap-std p-std">
    <TimelineItemGroup v-for="(value, key) in groups" :key="key" :title="key" :events="value" />
    <div class="text-center text-sm text-neutral-500">--- You have reached the beginning of time ---</div>
  </List>
</template>
