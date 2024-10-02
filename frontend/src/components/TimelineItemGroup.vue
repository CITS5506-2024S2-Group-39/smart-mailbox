<script setup lang="ts">
import Button from "@/components/common/Button.vue";
import Collapse from "@/components/common/Collapse.vue";
import Icon from "@/components/common/Icon.vue";
import List from "@/components/common/List.vue";
import TimelineItem from "@/components/TimelineItem.vue";
import { type MailboxEvent } from "@/types/MailboxEvent";
import { ref } from "vue";

const { title, events } = defineProps<{ title: string; events: MailboxEvent[] }>();
const collapsed = ref<boolean>(false);
</script>

<template>
  <div class="relative">
    <div class="pointer-events-none absolute -top-header-height">
      <!-- Anchor. The outer offset corresponds to the height of the header, -->
      <!-- and the inner offset corresponds to the padding of the main content -->
      <!-- refer to App.vue for details -->
      <div class="absolute desktop:-top-8 mobile:-top-4" :id="title"></div>
    </div>
    <Button
      class="flex items-center desktop:gap-4 desktop:px-6 desktop:py-4 desktop:transition-colors desktop:hoctive:bg-current/5
        mobile:gap-2 mobile:py-2"
      @click="collapsed = !collapsed"
    >
      <Icon
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
