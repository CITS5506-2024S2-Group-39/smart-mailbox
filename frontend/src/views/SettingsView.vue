<script setup lang="ts">
import Button from "@/components/common/Button.vue";
import Card from "@/components/common/Card.vue";
import LockControlDialog from "@/components/LockControlDialog.vue";
import PasswordUpdateDialog from "@/components/PasswordUpdateDialog.vue";
import SettingsItem from "@/components/SettingsItem.vue";
import deviceStatus from "@/stores/device-status";
import { shallowRef } from "vue";

const lockdialog = shallowRef<typeof LockControlDialog>();
const passworddialog = shallowRef<typeof PasswordUpdateDialog>();
</script>

<template>
  <div class="grid grid-cols-1 gap-std p-std">
    <Card title="Mailbox Management">
      <div class="text-sm text-neutral-500">Control the behavior of the mailbox.</div>

      <hr class="border-t border-neutral-200" />

      <div class="relative flex gap-std/2 desktop:flex-row mobile:flex-col">
        <div class="w-48 flex-none text-sm/8 font-bold desktop:order-1">Change Password</div>

        <div class="desktop:order-3 mobile:absolute mobile:right-0 mobile:top-0">
          <Button
            class="flex w-20 flex-row items-center justify-center gap-1 rounded-lg transition-colors hoctive:bg-current/5"
            @click="passworddialog!.show()"
          >
            <span class="text-sm/8">Update</span>
            <PasswordUpdateDialog ref="passworddialog" />
          </Button>
        </div>

        <div v-if="!deviceStatus.online" class="text-base/8 text-neutral-400 desktop:order-2 desktop:flex-1">
          Mailbox Offline
        </div>
        <div v-else class="text-base/8 desktop:order-2 desktop:flex-1">••••••••</div>
      </div>

      <hr class="border-t border-neutral-200" />

      <div class="relative flex gap-std/2 desktop:flex-row mobile:flex-col">
        <div class="w-48 flex-none text-sm/8 font-bold desktop:order-1">Lock Control</div>

        <div class="desktop:order-3 mobile:absolute mobile:right-0 mobile:top-0">
          <Button
            class="flex w-20 flex-row items-center justify-center gap-1 rounded-lg transition-colors hoctive:bg-current/5"
            @click="lockdialog!.show()"
          >
            <span class="text-sm/8">Manage</span>
            <LockControlDialog ref="lockdialog" />
          </Button>
        </div>

        <div v-if="!deviceStatus.online" class="text-base/8 text-neutral-400 desktop:order-2 desktop:flex-1">
          Mailbox Offline
        </div>
        <div v-else-if="deviceStatus.locked" class="text-base/8 desktop:order-2 desktop:flex-1">Mailbox Locked</div>
        <div v-else class="text-base/8 desktop:order-2 desktop:flex-1">Mailbox Unlocked</div>
      </div>
    </Card>

    <Card title="Notification Settings">
      <div class="text-sm text-neutral-500">Set up notification methods to be notified by new events.</div>

      <hr class="border-t border-neutral-200" />

      <SettingsItem
        title="Email Address"
        name="notification.email"
        placeholder="e.g. name@example.com"
        :spellcheck="false"
      />

      <hr class="border-t border-neutral-200" />

      <SettingsItem title="Phone Number" name="notification.phone" placeholder="e.g. 0412345678" :spellcheck="false" />
    </Card>
    <Card title="Prompt Settings">
      <div class="text-sm text-neutral-500">
        Enhance the smart mailbox's accuracy in mail cover recognition by supplying additional contextual information.
      </div>

      <hr class="border-t border-neutral-200" />

      <SettingsItem title="Country or Region" name="prompt.region" placeholder="e.g. Australia" />

      <hr class="border-t border-neutral-200" />

      <SettingsItem
        title="Mailbox Address"
        name="prompt.address"
        placeholder="e.g. 35 Stirling Highway, Perth, WA, 6009"
      />

      <hr class="border-t border-neutral-200" />

      <SettingsItem
        title="Known Recipients"
        name="prompt.users"
        placeholder="e.g. John Doe, Jane Smith, Greenfield Group, Fortune Family Investments"
        :spellcheck="false"
      />

      <hr class="border-t border-neutral-200" />

      <SettingsItem
        title="Additional Comments"
        name="prompt.comments"
        placeholder="e.g. I have subscribed to a newspaper that is usually delivered on Mondays"
        :rows="5"
      />
    </Card>
  </div>
</template>
