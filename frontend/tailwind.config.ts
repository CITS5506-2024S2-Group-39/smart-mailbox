import type { Config } from "tailwindcss";
import plugin from "tailwindcss/plugin";

// convert tailwind spacing unit to rem.
function toRem(space: number): string {
  const rem = 0.25 * space;
  return `${rem}rem`;
}

function generateSpacing(min: number, max: number, step: number): Record<number, string> {
  const result = {};
  for (let i = min; i <= max; i += step) {
    result[i] = toRem(i);
  }
  return result;
}

function colorMix(color: string, background: string, alpha: number): string {
  // Return a color-mix with the specified color, background, and alpha
  return `color-mix(in srgb, ${color} ${alpha}%, ${background})`;
}

function generateCurrentColor(): Record<string, string> {
  const result: Record<string, string> = {};

  // Generate color for current with varying opacity (bg-current/{opacity})
  for (let i = 0; i <= 100; ++i) {
    result[`current/${i}`] = colorMix("currentColor", "transparent", i);
  }

  // Generate color for current with varying intensity (bg-current-{intensity})
  for (const intensity of [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]) {
    result[`current-${intensity}`] = colorMix("currentColor", "white", intensity / 10);
  }

  return result;
}

const config: Config = {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontSize: generateSpacing(0, 256, 0.5),
      spacing: {
        ...generateSpacing(0, 256, 0.5),
        "navbar-width": "6rem", // Width for desktop view
        "navbar-height": "4rem", // Height for mobile view
        "header-height": "4rem", // Standard header height
        // TailwindCSS does not provide an easy method to define different spacing values for various screen sizes.
        // To address this, use CSS variables instead. Please also refer to main.css for more details.
        std: "var(--standard-spacing)", // Standard spacing value
        "std/2": "calc(var(--standard-spacing) / 2)", // Half of the standard spacing
      },
      screens: {
        desktop: { min: "1024px" },
        mobile: { max: "1023.999999px" },
      },
      colors: {
        ...generateCurrentColor(),
      },
      borderColor: {
        // Force user to specify a color explicitly
        DEFAULT: "currentColor",
      },
    },
  },
  plugins: [
    plugin(
      // custom variant
      function ({ addVariant }) {
        const add = (name, definition) => {
          addVariant(name, definition);
          addVariant(
            `group-${name}`,
            definition.map((x) => x.replace(/&/g, ".group") + " &"),
          );
        };
        add("hoctive", ["&:hover", "&:focus-visible", "&:active", "&.router-link-active"]);
        add("router-link-active", ["&.router-link-active"]);
        addVariant("pseudo", ["&:before", "&:after"]);
      },
    ),
  ],
};

export default config;
