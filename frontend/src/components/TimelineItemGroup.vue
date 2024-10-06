<script setup lang="ts">
import Button from "@/components/common/Button.vue";
import Card from "@/components/common/Card.vue";
import Collapse from "@/components/common/Collapse.vue";
import Icon from "@/components/common/Icon.vue";
import List from "@/components/common/List.vue";
import TimelineItem from "@/components/TimelineItem.vue";
import { type MailboxEvent } from "@/stores/events";
import { shallowRef } from "vue";

const { title, events } = defineProps<{ title: string; events: MailboxEvent[] }>();
const collapsed = shallowRef<boolean>(false);
</script>

<template>
  <Card>
    <!-- The -m-std negates the default padding of <Card>, allowing the use of hoctive color -->
    <div class="relative -m-std overflow-hidden">
      <div class="pointer-events-none absolute -top-header-height -m-std">
        <!--  Anchor. The -top-header-height corresponds to the header height of <App>, -->
        <!-- and the -m-std corresponds to the padding of <TimelineView> -->
        <div :id="title"></div>
      </div>
      <Button
        class="flex flex-row items-center gap-std p-std transition-colors hoctive:bg-current/5"
        @click="collapsed = !collapsed"
      >
        <Icon
          class="flex-none text-6 text-neutral-500 transition-transform"
          type="keyboard_arrow_down"
          :class="{ '-rotate-90': collapsed }"
        />
        <span class="flex-1 text-base font-bold" v-text="title"></span>
      </Button>
      <Collapse :collapsed="collapsed">
        <List>
          <TimelineItem v-for="event of events" :key="event.id" :event="event" />
        </List>
      </Collapse>
    </div>
  </Card>
</template>
