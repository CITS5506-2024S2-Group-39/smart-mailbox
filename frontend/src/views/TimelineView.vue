<script setup lang="ts">
import TimelineItemGroup from "@/components/TimelineItemGroup.vue";

import type { MailboxEvent } from "@/types/MailboxEvent";

function groupEventsByDate(events: MailboxEvent[]): Record<string, MailboxEvent[]> {
  const groupedEvents: Record<string, MailboxEvent[]> = {};

  for (const event of events) {
    const eventDate = new Date(event.time);
    const dateKey = eventDate.toLocaleDateString(undefined, {
      month: "short",
      day: "numeric",
      year: "numeric",
    });

    if (!groupedEvents[dateKey]) {
      groupedEvents[dateKey] = [event];
    } else {
      groupedEvents[dateKey].push(event);
    }
  }

  return groupedEvents;
}

import data from "@/mock/events";
let groups = groupEventsByDate(data);
</script>

<template>
  <template v-for="(value, key) in groups">
    <TimelineItemGroup :title="key" :events="value" />
  </template>
</template>
