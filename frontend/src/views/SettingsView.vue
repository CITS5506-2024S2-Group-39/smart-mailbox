<script setup lang="ts">
import Button from "@/components/common/Button.vue";
import Card from "@/components/common/Card.vue";
import Icon from "@/components/common/Icon.vue";
</script>

<template>
  <div class="grid grid-cols-1 gap-std p-std">
    <Card title="Mailbox Management">
      <div class="text-sm text-neutral-500">Control the behavior of the mailbox.</div>

      <hr class="border-t border-neutral-200" />

      <div class="flex gap-std/2 desktop:flex-row desktop:items-center mobile:flex-col">
        <div class="desktop:contents mobile:flex mobile:flex-row mobile:items-center mobile:justify-between">
          <div class="text-sm font-bold desktop:order-1 desktop:w-48">Mailbox Password</div>
          <Button
            class="flex flex-row items-center justify-center gap-1 rounded-lg px-4 py-2 text-sm transition-colors hoctive:bg-current/5
              desktop:order-3"
          >
            <Icon type="edit" />
            Update
          </Button>
        </div>
        <input class="text-base/loose desktop:order-2 desktop:flex-1" placeholder="••••••••" />
      </div>

      <hr class="border-t border-neutral-200" />

      <div class="flex gap-std/2 desktop:flex-row desktop:items-center mobile:flex-col">
        <div class="desktop:contents mobile:flex mobile:flex-row mobile:items-center mobile:justify-between">
          <div class="text-sm font-bold desktop:order-1 desktop:w-48">Lock Control</div>
          <Button
            class="flex flex-row items-center justify-center gap-1 rounded-lg px-4 py-2 text-sm transition-colors hoctive:bg-current/5
              desktop:order-3"
          >
            <Icon type="lock_open" />
            Unlock
          </Button>
        </div>
        <input class="text-base/loose desktop:order-2 desktop:flex-1" placeholder="Locked" />
      </div>
    </Card>

    <Card title="Notification Settings">
      <div class="text-sm text-neutral-500">Set up notification methods to be notified by new events.</div>

      <hr class="border-t border-neutral-200" />

      <div class="flex gap-std/2 desktop:flex-row desktop:items-center mobile:flex-col">
        <div class="desktop:contents mobile:flex mobile:flex-row mobile:items-center mobile:justify-between">
          <div class="text-sm font-bold desktop:order-1 desktop:w-48">Email Address</div>
          <Button
            class="flex flex-row items-center justify-center gap-1 rounded-lg px-4 py-2 text-sm transition-colors hoctive:bg-current/5
              desktop:order-3"
          >
            <Icon type="edit" />
            Edit
          </Button>
        </div>
        <input class="text-base/loose desktop:order-2 desktop:flex-1" placeholder="e.g. name@example.com" />
      </div>

      <hr class="border-t border-neutral-200" />

      <div class="flex gap-std/2 desktop:flex-row desktop:items-center mobile:flex-col">
        <div class="desktop:contents mobile:flex mobile:flex-row mobile:items-center mobile:justify-between">
          <div class="text-sm font-bold desktop:order-1 desktop:w-48">Phone Number</div>
          <Button
            class="flex flex-row items-center justify-center gap-1 rounded-lg px-4 py-2 text-sm transition-colors hoctive:bg-current/5
              desktop:order-3"
          >
            <Icon type="edit" />
            Edit
          </Button>
        </div>
        <input class="text-base/loose desktop:order-2 desktop:flex-1" placeholder="e.g. 0412345678" />
      </div>
    </Card>
    <Card title="Prompt Settings">
      <div class="text-sm text-neutral-500">
        Enhance the smart mailbox's accuracy in mail cover recognition by supplying additional contextual information.
      </div>

      <hr class="border-t border-neutral-200" />

      <div class="flex gap-std/2 desktop:flex-row desktop:items-center mobile:flex-col">
        <div class="desktop:contents mobile:flex mobile:flex-row mobile:items-center mobile:justify-between">
          <div class="text-sm font-bold desktop:order-1 desktop:w-48">Mailbox Address</div>
          <Button
            class="flex flex-row items-center justify-center gap-1 rounded-lg px-4 py-2 text-sm transition-colors hoctive:bg-current/5
              desktop:order-3"
          >
            <Icon type="edit" />
            Edit
          </Button>
        </div>
        <input
          class="text-base/loose desktop:order-2 desktop:flex-1"
          placeholder="e.g. 35 Stirling Highway, Perth, WA, 6009"
        />
      </div>

      <hr class="border-t border-neutral-200" />

      <div class="flex gap-std/2 desktop:flex-row desktop:items-center mobile:flex-col">
        <div class="desktop:contents mobile:flex mobile:flex-row mobile:items-center mobile:justify-between">
          <div class="text-sm font-bold desktop:order-1 desktop:w-48">Possible Recipients</div>
          <Button
            class="flex flex-row items-center justify-center gap-1 rounded-lg px-4 py-2 text-sm transition-colors hoctive:bg-current/5
              desktop:order-3"
          >
            <Icon type="edit" />
            Edit
          </Button>
        </div>
        <input
          class="text-base/loose desktop:order-2 desktop:flex-1"
          placeholder="e.g. John Doe, Jane Smith, Greenfield Group, Fortune Family Investments"
        />
      </div>

      <hr class="border-t border-neutral-200" />

      <div class="flex gap-std/2 desktop:flex-row desktop:items-center mobile:flex-col">
        <div class="desktop:contents mobile:flex mobile:flex-row mobile:items-center mobile:justify-between">
          <div class="text-sm font-bold desktop:order-1 desktop:w-48">Additional Comments</div>
          <Button
            class="flex flex-row items-center justify-center gap-1 rounded-lg px-4 py-2 text-sm transition-colors hoctive:bg-current/5
              desktop:order-3"
          >
            <Icon type="edit" />
            Edit
          </Button>
        </div>
        <input
          class="text-base/loose desktop:order-2 desktop:flex-1"
          placeholder="e.g. I have subscribed to a newspaper that is usually delivered on Mondays"
        />
      </div>
    </Card>
  </div>
</template>
