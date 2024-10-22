<script setup lang="ts">
import Button from "@/components/common/Button.vue";
import Card from "@/components/common/Card.vue";
import { postAPI } from "@/api";
import deviceStatus from "@/stores/device-status";
import { showSuccess } from "@/stores/toast";
import { shallowRef } from "vue";

const show = shallowRef<boolean>(false);

const showDialog = () => {
  show.value = true;
};

const hideDialog = () => {
  show.value = false;
};

defineExpose({
  show: showDialog,
  close: hideDialog,
});

const setLockState = (locked: boolean) => {
  postAPI("/api/mailbox/lock", { locked: locked }, () => {
    showSuccess("Operation issued successfully");
    hideDialog();
  });
};
</script>

<template>
  <div v-if="show" class="fixed inset-0 z-30 grid place-items-center bg-neutral-950/50 p-std" @click.prevent.stop>
    <Card title="Confirm Operation" class="desktop:w-136 mobile:w-full">
      <template v-if="!deviceStatus.online">
        <div>
          <div>
            <span class="font-bold">NOTE:</span>
            Mailbox is
            <span class="font-bold">offline</span>
            currently.
          </div>
          <div>The opeartion will be executed once the mailbox is online.</div>
        </div>
        <div class="flex flex-row gap-std/2">
          <Button class="rounded-lg bg-neutral-900 p-3 text-sm/none text-white" @click="setLockState(true)">
            Lock
          </Button>
          <Button class="rounded-lg bg-neutral-900 p-3 text-sm/none text-white" @click="setLockState(false)">
            Unlock
          </Button>
          <div class="flex-1"></div>
          <Button class="rounded-lg border p-3 text-sm/none" @click="hideDialog()">Cancel</Button>
        </div>
      </template>
      <template v-else>
        <div>
          <div>
            Mailbox is
            <span class="font-bold">{{ deviceStatus.locked ? "locked" : "unlocked" }}</span>
            currently.
          </div>
          <div>
            Are you sure you want to
            <span class="font-bold">
              {{ deviceStatus.locked ? "unlock" : "lock" }}
            </span>
            the mailbox?
          </div>
        </div>
        <div class="flex flex-row gap-std/2">
          <Button
            class="rounded-lg bg-neutral-900 p-3 text-sm/none text-white"
            @click="setLockState(!deviceStatus.locked)"
          >
            Confirm
          </Button>
          <div class="flex-1"></div>
          <Button class="rounded-lg border p-3 text-sm/none" @click="hideDialog()">Cancel</Button>
        </div>
      </template>
    </Card>
  </div>
</template>
