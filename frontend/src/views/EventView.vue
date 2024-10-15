<script setup lang="ts">
import AspectRatio from "@/components/common/AspectRatio.vue";
import Button from "@/components/common/Button.vue";
import Card from "@/components/common/Card.vue";
import Icon from "@/components/common/Icon.vue";
import Image from "@/components/common/Image.vue";
import TextArea from "@/components/common/TextArea.vue";
import MailboxEventIcon from "@/components/MailboxEventIcon.vue";
import { getAPI, postAPI } from "@/api";
import { type MailboxEvent, EventType, MailTypes, fullUpdate } from "@/stores/events";
import { showSuccess } from "@/stores/toast";
import { reactive, ref } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const event = reactive<MailboxEvent>({ id: 0 } as MailboxEvent);

const updateEvent = () => {
  const data = event.data;
  postAPI(`/api/event/${route.params.id}`, data, () => {
    showSuccess("Event detail updated successfully");
    fullUpdate(); // refresh event list so other parts will be reflected
    return;
  });
};

getAPI(`/api/event/${route.params.id}`, (data: MailboxEvent) => {
  data.time = new Date(data.time);
  Object.assign(event, data);
  return;
});
</script>

<template>
  <div class="flex flex-col gap-std p-std" v-if="event.id">
    <Card class="relative">
      <div class="flex flex-row items-center gap-std">
        <div
          class="grid place-items-center rounded-full border-[2px] border-neutral-200 desktop:size-32 mobile:size-16"
        >
          <MailboxEventIcon :type="event.type" class="desktop:text-24 mobile:text-12" />
        </div>
        <div class="flex flex-1 flex-col gap-std/2">
          <div v-text="event.type" class="font-bold desktop:text-8/none mobile:text-6/none"></div>
          <div v-text="event.time.toLocaleString()" class="text-sm/none text-neutral-500"></div>
        </div>
      </div>

      <template v-if="event.data.image">
        <Image
          :src="'/api/images/' + event.data.image"
          class="aspect-[4/3] desktop:absolute desktop:right-std desktop:top-std desktop:h-32"
        />
      </template>

      <hr class="border-t border-neutral-200" />

      <div class="flex gap-std/2 desktop:flex-row mobile:flex-col">
        <label class="w-48 flex-none text-sm/8 font-bold">Summary</label>
        <TextArea name="summary" v-model="event.data.summary" class="w-full py-1 text-base"></TextArea>
      </div>

      <template v-if="event.type === EventType.MailboxIncomingMail">
        <hr class="border-t border-neutral-200" />

        <div class="flex gap-std/2 desktop:flex-row mobile:flex-col">
          <label class="w-48 flex-none text-sm/8 font-bold">Recipient Name</label>
          <input class="flex-1 text-base/8" placeholder="None" v-model="event.data.recipient_name" />
        </div>

        <hr class="border-t border-neutral-200" />

        <div class="flex gap-std gap-std/2 desktop:flex-row mobile:flex-col">
          <label class="w-48 flex-none text-sm/8 font-bold">Recipient Address</label>

          <div class="flex flex-1 flex-col gap-std/2 mobile:contents">
            <div class="flex flex-row gap-std/2">
              <label class="w-24 flex-none text-sm/8 font-bold">Street</label>
              <input class="flex-1 text-base/8" placeholder="None" v-model="event.data.recipient_address.street" />
            </div>
            <div class="flex flex-row gap-std/2">
              <label class="w-24 flex-none text-sm/8 font-bold">City</label>
              <input class="flex-1 text-base/8" placeholder="None" v-model="event.data.recipient_address.city" />
            </div>
          </div>

          <div class="mobile:hidden"></div>

          <div class="flex flex-1 flex-col gap-std/2 mobile:contents">
            <div class="flex flex-row gap-std/2">
              <label class="w-24 flex-none text-sm/8 font-bold">State</label>
              <input class="flex-1 text-base/8" placeholder="None" v-model="event.data.recipient_address.state" />
            </div>
            <div class="flex flex-row gap-std/2">
              <label class="w-24 flex-none text-sm/8 font-bold">Postcode</label>
              <input class="flex-1 text-base/8" placeholder="None" v-model="event.data.recipient_address.postal_code" />
            </div>
          </div>
        </div>

        <hr class="border-t border-neutral-200" />

        <div class="flex gap-std/2 desktop:flex-row mobile:flex-col">
          <label class="w-48 flex-none text-sm/8 font-bold">Sender Name</label>
          <input class="flex-1 text-base/8" placeholder="None" v-model="event.data.sender_name" />
        </div>

        <hr class="border-t border-neutral-200" />

        <div class="flex gap-std gap-std/2 desktop:flex-row mobile:flex-col">
          <label class="w-48 flex-none text-sm/8 font-bold">Sender Address</label>

          <div class="flex flex-1 flex-col gap-std/2 mobile:contents">
            <div class="flex flex-row gap-std/2">
              <label class="w-24 flex-none text-sm/8 font-bold">Street</label>
              <input class="flex-1 text-base/8" placeholder="None" v-model="event.data.sender_address.street" />
            </div>
            <div class="flex flex-row gap-std/2">
              <label class="w-24 flex-none text-sm/8 font-bold">City</label>
              <input class="flex-1 text-base/8" placeholder="None" v-model="event.data.sender_address.city" />
            </div>
          </div>

          <div class="mobile:hidden"></div>

          <div class="flex flex-1 flex-col gap-std/2 mobile:contents">
            <div class="flex flex-row gap-std/2">
              <label class="w-24 flex-none text-sm/8 font-bold">State</label>
              <input class="flex-1 text-base/8" placeholder="None" v-model="event.data.sender_address.state" />
            </div>
            <div class="flex flex-row gap-std/2">
              <label class="w-24 flex-none text-sm/8 font-bold">Postcode</label>
              <input class="flex-1 text-base/8" placeholder="None" v-model="event.data.sender_address.postal_code" />
            </div>
          </div>
        </div>

        <hr class="border-t border-neutral-200" />

        <div class="flex gap-std/2 desktop:flex-row mobile:flex-col">
          <label class="w-48 flex-none text-sm/8 font-bold">Tracking Number</label>
          <input class="flex-1 text-base/8" placeholder="None" v-model="event.data.tracking_number" />
        </div>

        <hr class="border-t border-neutral-200" />

        <div class="flex gap-std/2 desktop:flex-row mobile:flex-col">
          <label class="w-48 flex-none text-sm/8 font-bold">Postage Information</label>
          <input class="flex-1 text-base/8" placeholder="None" v-model="event.data.postage_information" />
        </div>

        <hr class="border-t border-neutral-200" />

        <div class="flex gap-std/2 desktop:flex-row mobile:flex-col">
          <label class="w-48 flex-none text-sm/8 font-bold">Mail Type</label>

          <select class="bg-transparent text-base/8" v-model="event.data.mail_type">
            <option v-for="type in MailTypes" :value="type" v-text="type"></option>
          </select>
        </div>
      </template>

      <hr class="border-t border-neutral-200" />

      <div class="flex gap-std/2 desktop:flex-row desktop:justify-end mobile:contents">
        <Button
          class="flex flex-row items-center justify-center gap-1 rounded-lg bg-neutral-800 p-3 text-white"
          @click="updateEvent"
        >
          <Icon type="save" class="text-4" />
          <span class="text-base/none">Update Event Details</span>
        </Button>
        <RouterLink to="/timeline" class="flex flex-row items-center justify-center gap-1 rounded-lg border p-3">
          <Icon type="arrow_back" class="text-4" />
          <span class="text-base/none">Return To Timeline</span>
        </RouterLink>
      </div>
    </Card>
  </div>
</template>
