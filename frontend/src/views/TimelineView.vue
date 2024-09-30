<script setup lang="ts">
import TimelineItemGroup from "@/components/TimelineItemGroup.vue";
import { requestAPI } from "@/api";
import { showSuccess } from "@/stores/toast";
import type { MailboxEvent } from "@/types/MailboxEvent";
import { setIntervalWithCancel } from "@/utils/timeout";
import { ref, computed, onBeforeUnmount } from "vue";

// All mailbox events to display
const events = ref<MailboxEvent[]>([]);

// Mailbox events grouped by date
const groups = computed(() => {
  const { value } = events;
  const map: Record<string, MailboxEvent[]> = {};
  for (const event of value) {
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

// Handler to load latest events list from backend
const update = () => {
  requestAPI("/api/events", undefined, (data: MailboxEvent[]) => {
    for (const event of data) {
      // Convert JSON format to Date object
      const time = event.time;
      event.time = new Date(time);
    }
    events.value = data;
  });
};

// Load initial data
update();

// Refresh data with a certain interval
// A possible optimization could be only loading updates
// However, it will be tricky because content of existing items could also be updated
// Avoiding premature optimization for now
const interval = 10 * 1000;
const cancel = setIntervalWithCancel(update, interval);

// Cancel interval when component is being destroyed
onBeforeUnmount(cancel);
</script>

<template>
  <section>
    <TimelineItemGroup v-for="(value, key) in groups" :title="key" :events="value" />
  </section>
</template>
