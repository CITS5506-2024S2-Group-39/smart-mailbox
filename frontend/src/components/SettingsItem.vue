<script setup lang="ts">
import Button from "@/components/common/Button.vue";
import Icon from "@/components/common/Icon.vue";
import settings, { updateSetting } from "@/stores/settings";
import { shallowRef } from "vue";

const {
  title,
  name,
  placeholder,
  spellcheck = true,
  rows = 1,
} = defineProps<{
  title: string;
  name: string;
  placeholder: string;
  spellcheck?: boolean;
  rows?: number;
}>();

const inputbox = shallowRef<HTMLTextAreaElement>();
const editing = shallowRef<boolean>(false);

const startEdit = () => {
  editing.value = true;
};

const endEdit = (save: boolean) => {
  if (save) {
    const input = inputbox.value as HTMLTextAreaElement;
    updateSetting(name, input.value);
  }
  editing.value = false;
};
</script>

<template>
  <div class="relative flex gap-std/2 desktop:flex-row mobile:flex-col">
    <div class="w-48 flex-none text-sm/8 font-bold desktop:order-1" v-text="title"></div>

    <div class="desktop:order-3 mobile:absolute mobile:right-0 mobile:top-0">
      <Button
        class="flex w-20 flex-row items-center justify-center gap-1 rounded-lg transition-colors hoctive:bg-current/5"
        :class="{ invisible: editing }"
        @click="startEdit"
      >
        <Icon type="edit" class="text-3.5" />
        <span class="text-sm/8">Edit</span>
      </Button>
    </div>

    <div
      v-if="!editing"
      class="overflow-x-hidden break-words py-1 text-base/6 desktop:order-2 desktop:flex-1"
      v-text="!settings[name] ? placeholder : settings[name]"
      :class="{ 'text-neutral-400': !settings[name] }"
    ></div>

    <div v-else class="flex flex-col gap-std/2 desktop:order-2 desktop:flex-1">
      <textarea
        ref="inputbox"
        :rows
        class="w-full rounded-lg border p-2 text-base/6"
        :spellcheck
        :placeholder
        :value="settings[name] || ''"
      ></textarea>
      <div class="flex flex-row gap-std/2">
        <Button
          class="relative rounded-lg bg-neutral-900 px-3 text-white after:absolute after:inset-0 after:transition-colors
            hoctive:after:bg-current/5"
          @click="endEdit(true)"
        >
          <span class="text-sm/8">Save</span>
        </Button>
        <Button class="rounded-lg border px-3 transition-colors hoctive:bg-current/5" @click="endEdit(false)">
          <span class="text-sm/8">Cancel</span>
        </Button>
      </div>
    </div>
  </div>
</template>
