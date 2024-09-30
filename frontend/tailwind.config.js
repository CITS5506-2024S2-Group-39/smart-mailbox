import colors from "tailwindcss/colors";
import plugin from "tailwindcss/plugin";

// convert tailwind spacing unit to rem.
function toRem(space) {
  let rem = 0.25 * space;
  return `${rem}rem`;
}

function generateSpacing(min, max, step) {
  let result = {};
  for (let i = min; i <= max; i += step) {
    result[i] = toRem(i);
  }
  return result;
}

function generateCurrentColorAlpha() {
  let result = {};
  for (let i = 0; i <= 100; ++i) {
    result[`current/${i}`] = `color-mix(in srgb, currentColor ${i}%, transparent)`;
  }
  return result;
}

/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontSize: generateSpacing(0, 128, 0.5),
      spacing: {
        ...generateSpacing(0, 128, 0.5),
        "navbar-width": toRem(24), // for desktop
        "navbar-height": toRem(16), // for mobile
        "header-height": toRem(16),
      },
      screens: {
        desktop: { min: "1024px" },
        mobile: { max: "1023.999999px" },
      },
      colors: {
        ...generateCurrentColorAlpha(),
      },
    },
  },
  plugins: [
    plugin(
      // custom variant
      function ({ addVariant }) {
        addVariant("hoctive", ["&:hover", "&:focus-visible", "&:active"]);
        addVariant("group-hoctive", [".group:hover &", ".group:focus-visible &", ".group:active &"]);
        addVariant("router-link-active", "&.router-link-active");
      },
    ),
  ],
};
