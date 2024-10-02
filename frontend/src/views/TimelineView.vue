<script setup lang="ts">
import List from "@/components/common/List.vue";
import TimelineItemGroup from "@/components/TimelineItemGroup.vue";
import { requestAPI } from "@/api";
import events from "@/stores/events";
import { showSuccess } from "@/stores/toast";
import type { MailboxEvent } from "@/types/MailboxEvent";
import { setIntervalWithCancel } from "@/utils/timeout";
import { ref, computed, onBeforeUnmount } from "vue";

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
</script>

<template>
  <List>
    <TimelineItemGroup v-for="(value, key) in groups" :key="key" :title="key" :events="value" />
    <div class="text-center text-sm text-gray-500 desktop:mt-8 mobile:mt-4">
      --- You have reached the beginning of time ---
    </div>
  </List>
</template>
