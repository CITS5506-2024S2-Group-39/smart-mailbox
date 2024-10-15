<script setup lang="ts">
import Card from "@/components/common/Card.vue";
import events, { EventType, MailTypes, type MailboxEvent } from "@/stores/events";
import arrayEqual from "@/utils/array-equal";
import Chart, { type ChartConfiguration } from "chart.js/auto";
import { onBeforeUnmount, onMounted, shallowRef, watchEffect } from "vue";

const labels: string[] = [];
const data: number[] = [];

const configuration: ChartConfiguration<"doughnut", number[], string> = {
  type: "doughnut",
  data: {
    labels: labels,
    datasets: [{ data: data }],
  },
  options: {
    responsive: true,
    aspectRatio: 5 / 4,
    plugins: {
      legend: { display: false },
    },
  },
};

const updateDataset = () => {
  let count: Record<string, number> = {};

  for (const event of events) {
    if (event.type !== EventType.MailboxIncomingMail) {
      continue;
    }
    let name = event.data.recipient_name;
    if (typeof name !== "string") name = "Not Recognized";
    let existing_count = count[name] || 0;
    count[name] = existing_count + 1;
  }

  let new_labels: string[] = Object.keys(count);
  let new_data: number[] = new_labels.map((k) => count[k]);

  if (arrayEqual(new_labels, labels) && arrayEqual(new_data, data)) {
    return false;
  }

  labels.splice(0, labels.length, ...new_labels);
  data.splice(0, data.length, ...new_data);
  return true;
};

const figure = shallowRef<HTMLCanvasElement>();

onMounted(() => {
  const canvas = figure.value as HTMLCanvasElement;
  let chart: Chart<"doughnut", number[], string> | null = null;

  watchEffect(() => {
    let changed = updateDataset();
    if (!changed) return;
    chart?.destroy();
    chart = new Chart<"doughnut", number[], string>(canvas, configuration);
  });

  onBeforeUnmount(() => chart?.destroy());
});
</script>

<template>
  <Card title="Distribution by Recipient">
    <canvas ref="figure"></canvas>
  </Card>
</template>
