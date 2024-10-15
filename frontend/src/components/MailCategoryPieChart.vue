<script setup lang="ts">
import Card from "@/components/common/Card.vue";
import events, { EventType, MailTypes, type MailboxEvent } from "@/stores/events";
import Chart, { type ChartConfiguration } from "chart.js/auto";
import { onBeforeUnmount, onMounted, shallowRef, watchEffect } from "vue";

const labels: string[] = MailTypes;
const data: number[] = labels.map((x) => 0);

const configuration: ChartConfiguration<"pie", number[], string> = {
  type: "pie",
  data: {
    labels: labels,
    datasets: [{ data: data }],
  },
  options: {
    responsive: true,
    aspectRatio: 2,
    plugins: {
      legend: { display: true, position: "right" },
    },
  },
};

const updateDataset = () => {
  let count: Record<string, number> = {};

  for (const event of events) {
    if (event.type !== EventType.MailboxIncomingMail) {
      continue;
    }
    let type = event.data.mail_type;
    if (typeof type !== "string") continue;
    type = type.toLowerCase();
    let existing_count = count[type] || 0;
    count[type] = existing_count + 1;
  }

  // Only update chart if there is a change
  let changed = false;

  for (let i = 0, n = labels.length; i < n; ++i) {
    let type = labels[i];
    type = type.toLowerCase();
    let oldval = data[i];
    let newval = count[type] || 0;
    data[i] = newval;
    if (newval !== oldval) {
      changed = true;
    }
  }

  return changed;
};

const figure = shallowRef<HTMLCanvasElement>();

onMounted(() => {
  const canvas = figure.value as HTMLCanvasElement;
  const chart = new Chart<"pie", number[], string>(canvas, configuration);
  watchEffect(() => updateDataset() && chart.update());
  onBeforeUnmount(() => chart.destroy());
});
</script>

<template>
  <Card title="Distribution of Mail Categories">
    <canvas ref="figure"></canvas>
  </Card>
</template>
