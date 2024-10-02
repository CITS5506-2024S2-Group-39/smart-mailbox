<script setup lang="ts">
import Card from "@/components/common/Card.vue";
import MonthSelector from "@/components/MonthSelector.vue";
import router from "@/router";
import events from "@/stores/events";
import { EventType, type MailboxEvent } from "@/types/MailboxEvent";
import arrayEqual from "@/utils/array-equal";
import Chart, { type ChartConfigurationCustomTypesPerDataset } from "chart.js/auto";
import type { ActiveElement, ChartEvent } from "chart.js/auto";
import colors from "tailwindcss/colors";
import { onMounted, onBeforeUnmount, shallowRef, watchEffect } from "vue";

function statisticForMonth(events: MailboxEvent[], normalizedMonthObject: Date): [string[], number[]] {
  const year = normalizedMonthObject.getFullYear();
  const zmonth = normalizedMonthObject.getMonth();

  // Assume normalizedMonthObject is a value normalized by <MonthSelector />.
  // It represents the last day of the month, enabling us to retrieve the number of days in that month.
  const days = normalizedMonthObject.getDate();
  const arraylike = { length: days };

  const labels: string[] = Array.from(
    arraylike, //
    (_, index) => new Date(year, zmonth, index + 1).toLocaleDateString(),
  );
  const data: number[] = Array.from(
    arraylike, //
    () => 0, // Zero count for each day
  );

  for (const { type, time } of events) {
    if (type !== EventType.MailboxIncomingMail) {
      continue;
    }
    if (year !== time.getFullYear()) {
      continue;
    }
    if (zmonth !== time.getMonth()) {
      continue;
    }
    const day = time.getDate(); // [1, ...]
    data[day - 1] += 1;
  }

  return [labels, data];
}

const month = shallowRef<Date>(
  // Use default value in child <MonthSelector />
  // This reference must be accessed after the child is initialized
  new Date(NaN),
);

// Will be populated when data becomes available
const labels: string[] = [];
const data: number[] = [];

const updateDataset = () => {
  const [days, counts] = statisticForMonth(events.value, month.value);

  // Do not update the dataset if it is unchanged.
  // This avoids unnecessary animations when the data remains the same.
  if (arrayEqual(days, labels) && arrayEqual(counts, data)) {
    return false;
  }

  // Update data and return
  labels.splice(0, labels.length, ...days);
  data.splice(0, data.length, ...counts);
  return true;
};

const onClick = (event: ChartEvent, elements: ActiveElement[], chart: Chart<"bar", number[], string>) => {
  // As we only have one dataset, there should be exactly one element that can be clicked at a time
  if (elements.length !== 1) {
    return;
  }

  // Retrieve the value associated with the element
  const [element] = elements;
  const { index } = element;
  const value = data[index];

  // If the value is not valid (In case it is not an expected integer, use !(value > 0) here)
  // Or is zero, there is no point to navigating to corresponding date in the timeline
  if (!(value > 0)) {
    return;
  }

  // Create a copy of the currently selected month
  // and set it as the date corresponding to the element
  const date = new Date(month.value);
  date.setDate(index + 1);

  // Get anchor and navigate to corresponding date in the timeline
  const anchor = date.toLocaleDateString();
  router.push({ path: "/timeline", hash: "#" + anchor });
};

const configuration: ChartConfigurationCustomTypesPerDataset<"bar", number[], string> = {
  data: {
    xLabels: labels,
    datasets: [
      {
        type: "bar",
        backgroundColor: colors.blue["500"],
        borderWidth: 0,
        data: data,
        label: "Value", // Description on hover
        minBarLength: 4, // Display height for zero values
      },
    ],
  },
  options: {
    // Layout related
    layout: { padding: 0 },
    responsive: true,
    aspectRatio: 4,
    maintainAspectRatio: true,

    // Appearence related
    animation: { duration: 150 },
    plugins: {
      legend: { display: false },
      tooltip: { titleAlign: "center", bodyAlign: "center", displayColors: false },
    },
    scales: {
      x: { display: false },
      y: { display: false, suggestedMax: 2 },
    },

    // Interaction related
    interaction: { mode: "index", axis: "x", intersect: false },
    onClick: onClick,
  },
};

const figure = shallowRef<HTMLCanvasElement>();

onMounted(() => {
  const canvas = figure.value as HTMLCanvasElement;
  const chart = new Chart<"bar", number[], string>(canvas, configuration);
  watchEffect(() => updateDataset() && chart.update());
  onBeforeUnmount(() => chart.destroy());
});
</script>

<template>
  <Card>
    <template v-slot:title>Daily Mail Count</template>
    <template v-slot:additional>
      <MonthSelector v-model="month" />
    </template>
    <canvas ref="figure" class="flex-none"></canvas>
  </Card>
</template>
