<script setup lang="ts">
import Card from "@/components/common/Card.vue";
import events from "@/stores/events";
import { EventType } from "@/types/MailboxEvent";
import Weekdays from "@/utils/weekday";
import colors from "tailwindcss/colors";
import { computed } from "vue";
import { VueDataUi, type VueUiSkeletonConfig } from "vue-data-ui";
import { type VueUiHeatmapDatasetItem, type VueUiHeatmapConfig } from "vue-data-ui";
import "vue-data-ui/style.css";

// X axis ticks
// prettier-ignore
const Hours = [
  "00:00", "", "",
  "03:00", "", "",
  "06:00", "", "",
  "09:00", "", "",
  "12:00", "", "",
  "15:00", "", "",
  "18:00", "", "",
  "21:00", "", "",
];

// Config to customize component color
const colorConfig = {
  cold: colors.blue["50"],
  hot: colors.blue["500"],
};

// Config to display loading effect
const skeletonConfig: VueUiSkeletonConfig = {
  type: "heatmap",
  style: {
    animated: false,
    heatmap: { cellsX: 24, cellsY: 7, color: colorConfig.cold },
  },
};

// Config to display heatmap itself
const heatmapConfig: VueUiHeatmapConfig = {
  style: {
    layout: {
      cells: {
        colors: colorConfig,
        selected: { border: 0 },
        value: { show: false },
      },
      dataLabels: {
        xAxis: { show: true, values: Hours },
        yAxis: { show: true, values: Weekdays },
      },
      padding: { top: 0, right: 0, left: 0, bottom: 0 },
    },
    legend: { show: false },
    tooltip: { show: false },
  },
  userOptions: { show: false },
  table: { show: false },
};

// The component generates a scalable vector graphic but uses fixed pixel padding.
// When the component is scaled down on narrower screens, the padding becomes disproportionately large.
// Applying proportional padding (in %) fixes this issue
const styleFix = { padding: "1.75% 0 0 3%" };

const dataset = computed(() => {
  const result: VueUiHeatmapDatasetItem[] = Weekdays.map(() => {
    return {
      name: "", // Using axis values in heatmapConfig
      values: Hours.map(() => 0), // Zero count for each hour
    };
  });

  // VueUiHeatmap does not work correctly if there is no data
  // Add a counter here to count the number of data points
  let total = 0;

  for (const { type, time } of events.value) {
    if (type !== EventType.MailboxIncomingMail) {
      continue;
    }

    const weekday = time.getDay();
    const hour = time.getHours();
    result[weekday].values[hour] += 1;

    total += 1;
  }

  // If there is no valid data, use VueUiSkeleton instead
  if (total === 0) {
    return null;
  }

  return result;
});
</script>

<template>
  <Card title="Delivery Time Heatmap">
    <div class="pointer-events-none" v-if="dataset">
      <!-- Disabling pointer events for VueDataUi as nothing useful can be implemented yet -->
      <VueDataUi component="VueUiHeatmap" :dataset="dataset" :config="heatmapConfig" :style="styleFix" />
    </div>
    <div v-else class="relative">
      <VueDataUi component="VueUiSkeleton" :config="skeletonConfig" />
      <div class="absolute inset-0 flex items-center justify-center text-base">No Data</div>
    </div>
  </Card>
</template>
