<script setup lang="ts">
import MailCategoryPieChart from "@/components/MailCategoryPieChart.vue";
import MailCountBarChart from "@/components/MailCountBarChart.vue";
import MailDeliveryTimeHeatmap from "@/components/MailDeliveryTimeHeatmap.vue";
import MailRecipientPieChart from "@/components/MailRecipientPieChart.vue";
</script>

<template>
  <div class="grid gap-std p-std desktop:grid-cols-3 mobile:grid-cols-1">
    <MailCountBarChart class="desktop:col-span-2" />
    <MailCategoryPieChart class="desktop:col-span-1" />
    <MailRecipientPieChart class="desktop:col-span-1" />
    <MailDeliveryTimeHeatmap class="desktop:col-span-2" />
  </div>
</template>
