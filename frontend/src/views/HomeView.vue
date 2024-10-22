<script setup lang="ts">
import Button from "@/components/common/Button.vue";
import Card from "@/components/common/Card.vue";
import Icon from "@/components/common/Icon.vue";
import LockControlDialog from "@/components/LockControlDialog.vue";
import NumberDisplay from "@/components/NumberDisplay.vue";
import PasswordUpdateDialog from "@/components/PasswordUpdateDialog.vue";
import deviceStatus from "@/stores/device-status";
import events, { EventType } from "@/stores/events";
import now from "@/stores/now";
import { computed, shallowRef } from "vue";

const mailsSinceLastOpen = computed(() => {
  let count = 0;
  for (let event of events) {
    if (event.type === EventType.MailboxIncomingMail) {
      ++count;
    } else if (event.type === EventType.MailboxLocked) {
      break;
    }
  }
  return count;
});

const mailsSinceTimeBegins = computed(() => {
  let count = 0;
  for (let event of events) {
    if (event.type === EventType.MailboxIncomingMail) {
      ++count;
    }
  }
  return count;
});

const lastMailEvent = computed(() => {
  for (let event of events) {
    if (event.type === EventType.MailboxIncomingMail) {
      return event;
    }
  }

  return null;
});

function prettyPrintTimeInterval(startDate: Date, endDate: Date) {
  const diffInMs: number = endDate.getTime() - startDate.getTime(); // Difference in milliseconds

  // Define time intervals in milliseconds
  const msInSecond = 1000;
  const msInMinute = msInSecond * 60;
  const msInHour = msInMinute * 60;
  const msInDay = msInHour * 24;

  // Calculate each time component
  const days = Math.floor(diffInMs / msInDay);
  const hours = Math.floor((diffInMs % msInDay) / msInHour);
  const minutes = Math.floor((diffInMs % msInHour) / msInMinute);
  const seconds = Math.floor((diffInMs % msInMinute) / msInSecond);

  // Create an array to hold the components
  const timeComponents = [];

  if (days > 0) timeComponents.push(`${days} day${days > 1 ? "s" : ""}`);
  if (hours > 0) timeComponents.push(`${hours} hour${hours > 1 ? "s" : ""}`);
  if (minutes > 0) timeComponents.push(`${minutes} minute${minutes > 1 ? "s" : ""}`);
  if (seconds > 0) timeComponents.push(`${seconds} second${seconds > 1 ? "s" : ""}`);

  // Join components with commas
  return timeComponents.length > 0 ? timeComponents.join(", ") : "0 seconds";
}

const lockdialog = shallowRef<typeof LockControlDialog>();
const passworddialog = shallowRef<typeof PasswordUpdateDialog>();
</script>

<template>
  <div class="grid gap-std p-std desktop:grid-cols-4 mobile:grid-cols-1">
    <Card class="desktop:order-1 desktop:col-span-2" title="Count of New Mails">
      <div class="flex flex-row desktop:gap-8 mobile:gap-4">
        <div class="flex basis-1/2 flex-col justify-between desktop:gap-8 mobile:gap-4">
          <div class="text-sm">Since Last Unlock</div>
          <div class="text-2xl/none font-bold">
            <NumberDisplay :value="mailsSinceLastOpen" />
          </div>
        </div>
        <div class="flex basis-1/2 flex-col justify-between desktop:gap-8 mobile:gap-4">
          <div class="text-sm">Lifetime Total</div>
          <div class="text-2xl/none font-bold">
            <NumberDisplay :value="mailsSinceTimeBegins" />
          </div>
        </div>
      </div>
    </Card>
    <Card class="desktop:order-3 desktop:col-span-2" title="Quick Actions">
      <div class="flex flex-row gap-std">
        <Button class="flex basis-1/2 flex-row items-center gap-2" @click="lockdialog!.show()">
          <Icon class="desktop:text-6 mobile:text-4" type="lock" />
          <span>Lock Control</span>
          <LockControlDialog ref="lockdialog" />
        </Button>
        <Button class="flex basis-1/2 flex-row items-center gap-2" @click="passworddialog!.show()">
          <Icon class="desktop:text-6 mobile:text-4" type="password" />
          <span>Change Password</span>
          <PasswordUpdateDialog ref="passworddialog" />
        </Button>
      </div>
    </Card>
    <Card class="desktop:order-4 desktop:col-span-2" title="Device Metric">
      <div class="flex flex-col gap-std/2">
        <div class="flex flex-row gap-std">
          <span class="w-24 flex-none text-sm font-bold">Status</span>
          <span class="break-none flex-1">
            {{ deviceStatus.online ? "Online" : "Offline" }}
          </span>
        </div>
        <div class="flex flex-row gap-std">
          <span class="w-24 flex-none text-sm font-bold">Uptime</span>
          <span class="break-none flex-1 text-nowrap">
            {{ deviceStatus.online ? prettyPrintTimeInterval(deviceStatus.since, now) : "N/A" }}
          </span>
        </div>
        <div class="flex flex-row gap-std">
          <span class="w-24 flex-none text-sm font-bold">Last Seen</span>
          <span class="break-none flex-1 text-nowrap">
            {{ deviceStatus.lastseen.getTime() ? deviceStatus.lastseen.toLocaleString() : "Never" }}
          </span>
        </div>
      </div>
    </Card>
    <Card class="desktop:order-2 desktop:col-span-2 desktop:row-span-3" title="Latest Mail">
      <template v-slot:additional>
        <div class="text-sm text-neutral-500" v-if="lastMailEvent" v-text="lastMailEvent.time.toLocaleString()"></div>
      </template>
      <div class="desktop:relative desktop:size-full desktop:overflow-auto">
        <div class="flex flex-col gap-std desktop:absolute desktop:inset-0">
          <template v-if="lastMailEvent">
            <img :src="'/api/images/' + lastMailEvent.data.image" class="aspect-[4/3] rounded-lg" />
            <div v-text="lastMailEvent.data.summary"></div>
          </template>
          <div v-else class="m-auto">No Data</div>
        </div>
      </div>
    </Card>
  </div>
</template>
