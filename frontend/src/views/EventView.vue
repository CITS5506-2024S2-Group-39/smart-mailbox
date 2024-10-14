<script setup lang="ts">
import AspectRatio from "@/components/common/AspectRatio.vue";
import Button from "@/components/common/Button.vue";
import Card from "@/components/common/Card.vue";
import Icon from "@/components/common/Icon.vue";
import TextArea from "@/components/common/TextArea.vue";
import MailboxEventIcon from "@/components/MailboxEventIcon.vue";
import { requestAPI } from "@/api";
import { type MailboxEvent, type MailEventData, EventType, MailTypes } from "@/stores/events";
import { reactive, ref } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const event = ref<MailboxEvent>();

requestAPI(`/api/event/${route.params.id}`, undefined, (data: MailboxEvent) => {
  console.log(data);

  data = {
    id: 1,
    time: new Date(),
    type: "New Mail",
    data: {
      summary:
        "The envelope is addressed to ZHaodong Shen at 56 Cleveland Court, Marangaroo, WA, 6064, likely from a bank located in Melbourne VIC, as suggested by the PO Box address. Thepostage is indicated as paid in Australia.",
      recipient_name: "Zhaodong Shen",
      recipient_address: {
        street: "56 Cleveland Court",
        city: "Marangaroo",
        state: "WA",
        postal_code: "6064",
      },
      sender_name: null,
      sender_address: {
        street: "Locked Bag 10",
        city: "Colins Street West",
        state: "Melbourne VIC",
        postal_code: "8007",
      },
      tracking_number: null,
      postage_information: "Postage Paid, Australia",
      mail_type: "Unknown",
    },
  };

  if (data.type === EventType.MailboxIncomingMail) {
    let details = data.data as MailEventData;
    details.recipient_name = details.recipient_name || null;
    details.recipient_address = details.recipient_address || {};
    details.recipient_address.street = details.recipient_address.street || null;
    details.recipient_address.city = details.recipient_address.city || null;
    details.recipient_address.state = details.recipient_address.state || null;
    details.recipient_address.postal_code = details.recipient_address.postal_code || null;
    details.sender_name = details.sender_name || null;
    details.sender_address = details.sender_address || {};
    details.sender_address.street = details.sender_address.street || null;
    details.sender_address.city = details.sender_address.city || null;
    details.sender_address.state = details.sender_address.state || null;
    details.sender_address.postal_code = details.sender_address.postal_code || null;
    details.tracking_number = details.tracking_number || null;
    details.postage_information = details.postage_information || null;
    details.mail_type = details.mail_type || "Unknown";
  }

  event.value = data;
  return;
});
</script>

<template>
  <div class="flex flex-col gap-std p-std" v-if="event">
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

      <AspectRatio
        ratio=" 4608 / 2592"
        class="bg-blue-100 desktop:absolute desktop:right-std desktop:top-std desktop:w-64"
      ></AspectRatio>

      <hr class="border-t border-neutral-200" />

      <div v-if="event.type !== EventType.MailboxIncomingMail">
        <div>
          <label class="w-48 flex-none text-sm/8 font-bold">Summary</label>
          <div v-text="event.data.summary"></div>
        </div>
      </div>

      <form v-else class="contents">
        <div class="flex gap-std/2 desktop:flex-row mobile:flex-col">
          <label class="w-48 flex-none text-sm/8 font-bold">Summary</label>
          <TextArea name="summary" v-model="event.data.summary" class="w-full py-1 text-base"></TextArea>
        </div>

        <hr class="border-t border-neutral-200" />

        <div class="flex gap-std/2 desktop:flex-row mobile:flex-col">
          <label class="w-48 flex-none text-sm/8 font-bold">Recipient Name</label>
          <input class="flex-1 text-base/8" placeholder="None" v-model="(event.data as MailEventData).recipient_name" />
        </div>

        <hr class="border-t border-neutral-200" />

        <div class="flex gap-std gap-std/2 desktop:flex-row mobile:flex-col">
          <label class="w-48 flex-none text-sm/8 font-bold">Recipient Address</label>

          <div class="flex flex-1 flex-col gap-std/2 mobile:contents">
            <div class="flex flex-row gap-std/2">
              <label class="w-24 flex-none text-sm/8 font-bold">Street</label>
              <input
                class="flex-1 text-base/8"
                placeholder="None"
                v-model="(event.data as MailEventData).recipient_address.street"
              />
            </div>
            <div class="flex flex-row gap-std/2">
              <label class="w-24 flex-none text-sm/8 font-bold">City</label>
              <input
                class="flex-1 text-base/8"
                placeholder="None"
                v-model="(event.data as MailEventData).recipient_address.city"
              />
            </div>
          </div>

          <div class="mobile:hidden"></div>

          <div class="flex flex-1 flex-col gap-std/2 mobile:contents">
            <div class="flex flex-row gap-std/2">
              <label class="w-24 flex-none text-sm/8 font-bold">State</label>
              <input
                class="flex-1 text-base/8"
                placeholder="None"
                v-model="(event.data as MailEventData).recipient_address.state"
              />
            </div>
            <div class="flex flex-row gap-std/2">
              <label class="w-24 flex-none text-sm/8 font-bold">Postcode</label>
              <input
                class="flex-1 text-base/8"
                placeholder="None"
                v-model="(event.data as MailEventData).recipient_address.postal_code"
              />
            </div>
          </div>
        </div>

        <hr class="border-t border-neutral-200" />

        <div class="flex gap-std/2 desktop:flex-row mobile:flex-col">
          <label class="w-48 flex-none text-sm/8 font-bold">Sender Name</label>
          <input class="flex-1 text-base/8" placeholder="None" v-model="(event.data as MailEventData).sender_name" />
        </div>

        <hr class="border-t border-neutral-200" />

        <div class="flex gap-std gap-std/2 desktop:flex-row mobile:flex-col">
          <label class="w-48 flex-none text-sm/8 font-bold">Sender Address</label>

          <div class="flex flex-1 flex-col gap-std/2 mobile:contents">
            <div class="flex flex-row gap-std/2">
              <label class="w-24 flex-none text-sm/8 font-bold">Street</label>
              <input
                class="flex-1 text-base/8"
                placeholder="None"
                v-model="(event.data as MailEventData).sender_address.street"
              />
            </div>
            <div class="flex flex-row gap-std/2">
              <label class="w-24 flex-none text-sm/8 font-bold">City</label>
              <input
                class="flex-1 text-base/8"
                placeholder="None"
                v-model="(event.data as MailEventData).sender_address.city"
              />
            </div>
          </div>

          <div class="mobile:hidden"></div>

          <div class="flex flex-1 flex-col gap-std/2 mobile:contents">
            <div class="flex flex-row gap-std/2">
              <label class="w-24 flex-none text-sm/8 font-bold">State</label>
              <input
                class="flex-1 text-base/8"
                placeholder="None"
                v-model="(event.data as MailEventData).sender_address.state"
              />
            </div>
            <div class="flex flex-row gap-std/2">
              <label class="w-24 flex-none text-sm/8 font-bold">Postcode</label>
              <input
                class="flex-1 text-base/8"
                placeholder="None"
                v-model="(event.data as MailEventData).sender_address.postal_code"
              />
            </div>
          </div>
        </div>

        <hr class="border-t border-neutral-200" />

        <div class="flex gap-std/2 desktop:flex-row mobile:flex-col">
          <label class="w-48 flex-none text-sm/8 font-bold">Tracking Number</label>
          <input
            class="flex-1 text-base/8"
            placeholder="None"
            v-model="(event.data as MailEventData).tracking_number"
          />
        </div>

        <hr class="border-t border-neutral-200" />

        <div class="flex gap-std/2 desktop:flex-row mobile:flex-col">
          <label class="w-48 flex-none text-sm/8 font-bold">Postage Information</label>
          <input
            class="flex-1 text-base/8"
            placeholder="None"
            v-model="(event.data as MailEventData).postage_information"
          />
        </div>

        <hr class="border-t border-neutral-200" />

        <div class="flex gap-std/2 desktop:flex-row mobile:flex-col">
          <label class="w-48 flex-none text-sm/8 font-bold">Mail Type</label>

          <select class="bg-transparent text-base/8" v-model="(event.data as MailEventData).mail_type">
            <option v-for="type in MailTypes" :value="type" v-text="type"></option>
          </select>
        </div>

        <hr class="border-t border-neutral-200" />

        <div class="flex gap-std/2 desktop:flex-row desktop:justify-end mobile:contents">
          <Button class="flex flex-row items-center justify-center gap-1 rounded-lg bg-neutral-800 p-3 text-white">
            <Icon type="save" class="text-4" />
            <span class="text-base/none">Update Event Details</span>
          </Button>
          <RouterLink to="/timeline" class="flex flex-row items-center justify-center gap-1 rounded-lg border p-3">
            <Icon type="arrow_back" class="text-4" />
            <span class="text-base/none">Return To Timeline</span>
          </RouterLink>
        </div>
      </form>
    </Card>
  </div>
</template>
