<script setup lang="ts">
import AspectRatio from "@/components/common/AspectRatio.vue";
import Card from "@/components/common/Card.vue";
import Icon from "@/components/common/Icon.vue";
import NumberDisplay from "@/components/NumberDisplay.vue";
import TimelineView from "./TimelineView.vue";
import events from "@/stores/events";
import { EventType } from "@/types/MailboxEvent";
import { computed } from "vue";

const mailsSinceLastOpen = computed(() => {
  let count = 0;
  for (let event of events.value) {
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
  for (let event of events.value) {
    if (event.type === EventType.MailboxIncomingMail) {
      ++count;
    }
  }
  return count;
});
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
    <Card class="desktop:order-3 desktop:col-span-1" title="Quick Actions">
      <div class="flex desktop:flex-col desktop:gap-4 mobile:flex-row mobile:gap-4">
        <div class="flex basis-1/2 desktop:flex-row desktop:gap-2 mobile:flex-col-reverse mobile:gap-4">
          <Icon class="text-2xl/none" type="lock" />
          <span>Unlock MailBox</span>
        </div>
        <div class="flex basis-1/2 desktop:flex-row desktop:gap-2 mobile:flex-col-reverse mobile:gap-4">
          <Icon class="text-2xl/none" type="password" />
          <span>Change Password</span>
        </div>
      </div>
    </Card>
    <Card class="desktop:order-4 desktop:col-span-1" title="Device Metric">
      <div class="desktop:relative desktop:size-full desktop:overflow-auto">
        <div class="desktop:absolute desktop:inset-0">
          <div class="flex flex-col desktop:gap-4 mobile:gap-4">
            <div class="flex flex-row desktop:gap-4 mobile:gap-4">
              <span class="flex-none basis-1/3 font-bold">Status</span>
              <span class="break-none flex-1 basis-2/3">Online</span>
            </div>
            <div class="flex flex-row desktop:gap-4 mobile:gap-4">
              <span class="flex-none basis-1/3 font-bold">Uptime</span>
              <span class="break-none flex-1 basis-2/3 text-nowrap">132 Day 8 Hours</span>
            </div>
          </div>
        </div>
      </div>
    </Card>
    <Card class="desktop:order-2 desktop:col-span-2 desktop:row-span-2" title="Latest Mail">
      <div class="desktop:relative desktop:size-full desktop:overflow-auto">
        <div class="flex flex-col gap-4 desktop:absolute desktop:inset-0">
          <AspectRatio ratio=" 4608 / 2592" class="bg-blue-100"></AspectRatio>
          <div>
            The mail cover shows the recipient, JOHN DOE, at 99 BAKER STREET, LONDON UK WC2N 5DU. The package is sent
            from PO BOX 789, MANCHESTER UK M3 1HP, and includes prepaid postage and tracking (GHI 234-5), indicating it
            is a business contract.
          </div>
        </div>
      </div>
    </Card>
  </div>
</template>
