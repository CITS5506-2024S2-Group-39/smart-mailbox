<script setup lang="ts">
import MailCategoryPieChart from "@/components/MailCategoryPieChart.vue";
import MailCountBarChart from "@/components/MailCountBarChart.vue";
import MailDeliveryTimeHeatmap from "@/components/MailDeliveryTimeHeatmap.vue";
</script>

<template>
  <div class="grid gap-std p-std desktop:grid-cols-3 mobile:grid-cols-1">
    <MailCountBarChart class="desktop:col-span-2" />
    <MailCategoryPieChart class="desktop:col-span-1" />
    <MailCategoryPieChart class="desktop:col-span-1" />
    <MailDeliveryTimeHeatmap class="desktop:col-span-2" />
  </div>
</template>
