<script setup lang="ts">
import Button from "@/components/common/Button.vue";
import Collapse from "@/components/common/Collapse.vue";
import List from "@/components/common/List.vue";
import MaterialIcon from "@/components/MaterialIcon.vue";
import TimelineItem from "@/components/TimelineItem.vue";
import { type MailboxEvent } from "@/types/MailboxEvent";
import { ref } from "vue";

const { title, events } = defineProps<{ title: string; events: MailboxEvent[] }>();
const collapsed = ref<boolean>(false);
</script>

<template>
  <div>
    <Button
      class="flex items-center desktop:gap-4 desktop:px-6 desktop:py-4 desktop:transition-colors desktop:hoctive:bg-current/5
        mobile:gap-2 mobile:py-2"
      @click="collapsed = !collapsed"
    >
      <MaterialIcon
        class="text-6 text-gray-500 transition-transform"
        type="keyboard_arrow_down"
        :class="{ '-rotate-90': collapsed }"
      />
      <span class="text-base font-bold" v-text="title"></span>
    </Button>
    <Collapse :collapsed="collapsed">
      <List>
        <TimelineItem v-for="event of events" :key="event.id" :event="event" />
      </List>
    </Collapse>
  </div>
</template>
