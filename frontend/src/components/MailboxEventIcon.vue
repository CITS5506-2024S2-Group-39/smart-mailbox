<script setup lang="ts">
import Icon from "@/components/common/Icon.vue";
import { EventType } from "@/stores/events";

const { type } = defineProps<{ type: string }>();
</script>

<template>
  <Icon v-if="type === EventType.MailboxIncomingMail" class="text-blue-500" type="mail" />
  <Icon v-else-if="type === EventType.MailboxUnlocked" class="text-green-500" type="lock_open" />
  <Icon v-else-if="type === EventType.MailboxLocked" class="text-red-500" type="lock" />
  <Icon v-else-if="type === EventType.MailboxPasswordChanged" class="text-pink-500" type="password" />
  <Icon v-else class="text-red-500" type="error" />
</template>
