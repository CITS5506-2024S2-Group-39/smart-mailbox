/** @type {import('tailwindcss').Config} */

function generateSpacing(min, max, step) {
  let result = {};
  for (let i = min; i <= max; i += step) {
    let r = 0.25 * i;
    result[i] = r + "rem";
  }
  return result;
}

export default {
  purge: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  content: [],
  theme: {
    extend: {
      fontSize: generateSpacing(0, 128, 0.5),
      spacing: generateSpacing(0, 128, 0.5),
    },
  },
  plugins: [],
};
