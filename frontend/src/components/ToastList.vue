<script setup lang="ts">
import Icon from "@/components/common/Icon.vue";
import List from "@/components/common/List.vue";
import { toasts } from "@/stores/toast";
import id from "@/utils/object-id";
</script>

<template>
  <aside
    class="pointer-events-none fixed right-0 top-0 z-50 flex max-h-screen flex-col pt-header-height desktop:w-112 mobile:w-screen
      mobile:pb-navbar-height"
    v-show="toasts.length"
  >
    <List class="pointer-events-auto flex flex-col gap-std overflow-y-auto p-std">
      <div
        v-for="toast in toasts"
        :key="id(toast)"
        class="flex flex-col gap-1 rounded-lg p-4 text-white"
        :class="{
          'bg-red-500': toast.icon === 'error', // error
          'bg-blue-500': toast.icon === 'info', // info
          'bg-green-500': toast.icon === 'check_circle', // success
        }"
      >
        <div class="flex flex-row items-center gap-2">
          <Icon :type="toast.icon" class="text-4" />
          <span class="text-base font-bold" v-text="toast.title"></span>
        </div>
        <div class="text-sm" v-text="toast.message"></div>
      </div>
    </List>
  </aside>
</template>
