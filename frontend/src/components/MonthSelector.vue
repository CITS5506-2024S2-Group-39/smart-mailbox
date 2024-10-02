<script setup lang="ts">
import Button from "@/components/common/Button.vue";
import Icon from "@/components/common/Icon.vue";

/**
 * Creates a Date object set to the last day of the specified month.
 *
 * @param {number} year - Must be in the range [1000, 9999].
 * @param {number} month - Must be in the range [1, 12].
 * @returns {Date} The Date object representing the last day of the specified month.
 *
 * This function sets the date to the last day of the specified month,
 * allowing the user to easily retrieve the number of days in the month using `date.getDate()`.
 */
function setMonth(year: number, month: number): Date {
  return new Date(year, month, 0);
}

/**
 * Gets year and month from a Date object.
 * Month will range in the range [1, 12] if the Date is valid.
 */
function getMonth(date: Date): [number, number] {
  const year: number = date.getFullYear();
  const month: number = date.getMonth() + 1; // [1, 12]
  return [year, month];
}

/**
 * Converts a Date object to a MM/YYYY string.
 */
function toMonthString(date: Date): string {
  const splitter = "/";
  const [year, month] = getMonth(date);
  const yyyy: string = String(year);
  const mm: string = String(month).padStart(2, "0");
  return mm + splitter + yyyy;
}

/**
 * Converts a MM/YYYY string to a Date object
 * The returned value is normalized with setMonth()
 */
function fromMonthString(str: string): Date | null {
  const splitter = "/";
  const splitted = str.split(splitter);
  if (splitted.length !== 2) {
    return null;
  }

  const [mm, yyyy] = splitted;
  const year = Number(yyyy);
  const month = Number(mm);
  if (!Number.isInteger(year) || !Number.isInteger(month)) {
    return null;
  }
  if (!(1000 <= year && year <= 9999)) {
    return null;
  }
  if (!(1 <= month && month <= 12)) {
    return null;
  }

  return setMonth(year, month);
}

const model = defineModel<Date>({ required: true });

{
  // Normalize the model value immediately whenever the instance becomes available.
  // However, the parent must wait until the instance is fully set up
  // before calling `model.getDate()` to retrieve the number of days in the selected month.
  const [year, month] = getMonth(model.value);

  if (!(1000 <= year && year <= 9999)) {
    // Provided value does not make sense, default to current month
    const current = new Date();
    const [year, month] = getMonth(current);
    model.value = setMonth(year, month);
  } else {
    // Normalize provided value
    model.value = setMonth(year, month);
  }
}

const handleTextInput = (event: FocusEvent | KeyboardEvent) => {
  const input = event.target as HTMLInputElement;
  input.blur(); // blur after completing the edit action
  const date = fromMonthString(input.value);

  if (!date) {
    // Selected month is invalid, do not update model
    // As model is not update, DOM will not be refreshed
    // Need to restore the displayed text in <input> here
    input.value = toMonthString(model.value);
  } else {
    // Selected month is valid, update model
    // Displayed text in <input> will be updated by reactivity
    model.value = date;
  }
};

const handleMonthAdjust = (delta: number) => {
  let [year, month] = getMonth(model.value);

  month += delta;
  if (month < 1) {
    month = 12;
    year -= 1;
  } else if (month > 12) {
    month = 1;
    year += 1;
  }

  if (!(1000 <= year && year <= 9999)) {
    // Selected month is invalid, do not update model
  } else {
    // Selected month is valid, update model
    // Displayed text in <input> will be updated by reactivity later
    model.value = setMonth(year, month);
  }
};
</script>

<template>
  <div class="flex flex-row items-center">
    <Button
      class="flex flex-none items-center justify-center desktop:transition-colors desktop:hoctive:bg-current/5"
      @click="handleMonthAdjust(-1)"
    >
      <Icon type="keyboard_arrow_left" class="text-6 text-gray-500" />
    </Button>
    <input
      type="text"
      size="7"
      class="flex-1 bg-transparent text-center text-base font-bold"
      :value="toMonthString(model)"
      @blur="handleTextInput($event)"
      @keydown.enter="handleTextInput($event)"
    />
    <Button
      class="flex flex-none items-center justify-center desktop:transition-colors desktop:hoctive:bg-current/5"
      @click="handleMonthAdjust(+1)"
    >
      <Icon type="keyboard_arrow_right" class="text-6 text-gray-500" />
    </Button>
  </div>
</template>
