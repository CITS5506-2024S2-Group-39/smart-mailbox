<script setup lang="ts">
import Card from "@/components/common/Card.vue";
</script>

<template>
  <div class="grid h-screen w-screen place-items-center overflow-auto p-std">
    <Card class="m-std w-full max-w-128">
      <div class="text-center">Logged in as: Admin</div>
      <Button class="flex flex-row items-center justify-center gap-1 rounded-lg bg-neutral-800 p-3 text-white">
        <Icon type="logout" class="text-4" />
        <span class="text-base/none">Logout</span>
      </Button>
    </Card>
  </div>
</template>
