<script setup lang="ts">
import { EventType } from "@/types/MailboxEvent";
import MaterialIcon from "@/components/MaterialIcon.vue";
const { type } = defineProps<{ type: string }>();
</script>

<template>
  <MaterialIcon v-if="type === EventType.MailboxIncomingMail" class="text-blue-500" type="mail" />
  <MaterialIcon v-else-if="type === EventType.MailboxUnlocked" class="text-green-500" type="lock_open" />
  <MaterialIcon v-else-if="type === EventType.MailboxLocked" class="text-red-500" type="lock" />
  <MaterialIcon v-else-if="type === EventType.MailboxPasswordChanged" class="text-pink-500" type="password" />
  <MaterialIcon v-else class="text-red-500" type="error" />
</template>
