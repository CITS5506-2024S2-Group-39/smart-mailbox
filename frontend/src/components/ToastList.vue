<script setup lang="ts">
import List from "@/components/common/List.vue";
import MaterialIcon from "@/components/MaterialIcon.vue";
import { toasts } from "@/stores/toast";
import id from "@/utils/object-id";
</script>

<template>
  <List class="flex flex-col gap-4 p-4">
    <div
      v-for="toast in toasts"
      :key="id(toast)"
      class="flex flex-col rounded-lg text-white desktop:gap-2 desktop:px-6 desktop:py-4 mobile:gap-1 mobile:px-4 mobile:py-2"
      :class="{
        'bg-red-500': toast.icon === 'error', // error
        'bg-blue-500': toast.icon === 'info', // info
        'bg-green-500': toast.icon === 'check_circle', // success
      }"
    >
      <div class="flex flex-row items-center gap-2">
        <MaterialIcon :type="toast.icon" class="text-4" />
        <span class="text-base font-bold" v-text="toast.title"></span>
      </div>
      <div class="text-sm" v-text="toast.message"></div>
    </div>
  </List>
</template>
