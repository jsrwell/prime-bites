/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{js,ts,jsx,tsx}", "./index.html"],
  theme: {
    extend: {
      colors: {
        "m-red": "#de1a1a",
        "m-brown": "#48392a",
        "m-orange": "#ea690d",
        "m-yellow": "#f5b700",
        "m-green": "#04a777",
        "m-gray": "#a49c93",
        "m-white": "#fffffc",
      },
    },
  },
  plugins: [],
};
