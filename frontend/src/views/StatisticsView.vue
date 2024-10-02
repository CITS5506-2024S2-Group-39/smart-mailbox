<script setup lang="ts">
import MailCategoryPieChart from "@/components/MailCategoryPieChart.vue";
import MailCountBarChart from "@/components/MailCountBarChart.vue";
import MailDeliveryTimeHeatmap from "@/components/MailDeliveryTimeHeatmap.vue";
</script>

<template>
  <div class="desktop:grid desktop:grid-cols-3 desktop:gap-8 mobile:flex mobile:flex-col mobile:gap-4">
    <MailCountBarChart class="desktop:col-span-2 mobile:flex-none" />
    <MailCategoryPieChart class="desktop:col-span-1 mobile:flex-none" />
    <MailCategoryPieChart class="desktop:col-span-1 mobile:flex-none" />
    <MailDeliveryTimeHeatmap class="desktop:col-span-2 mobile:flex-none" />
  </div>
</template>
