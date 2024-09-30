<script setup lang="ts">
import { useRoute } from "vue-router";

const route = useRoute();
</script>

<template>
  <div>
    EventView
    {{ route.params.id }}
  </div>
</template>
