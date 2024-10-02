// Get weekday string based on locale
export const toLocaleWeekdayString = (date: Date): string => {
  return date.toLocaleString(undefined, { weekday: "short" });
};

// Dynamically generate weekday names based on locale, avoid hardcoding specific weekday names
// Note: The index corresponds to the output of Date.getDay(), where 0 represents Sunday.
const Weekdays = [
  toLocaleWeekdayString(new Date(2024, 9, 6)), // Sunday (2024-10-06)
  toLocaleWeekdayString(new Date(2024, 9, 7)), // Monday (2024-10-07)
  toLocaleWeekdayString(new Date(2024, 9, 1)), // Tuesday (2024-10-01)
  toLocaleWeekdayString(new Date(2024, 9, 2)), // Wednesday (2024-10-02)
  toLocaleWeekdayString(new Date(2024, 9, 3)), // Thursday (2024-10-03)
  toLocaleWeekdayString(new Date(2024, 9, 4)), // Friday (2024-10-04)
  toLocaleWeekdayString(new Date(2024, 9, 5)), // Saturday (2024-10-05)
];

export default Weekdays;
