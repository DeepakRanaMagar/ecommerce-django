/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.{htm, js}',
  ],
  theme: {
    extend: {
      fontFamily: {
        display: ["Gloock", serif],
      }
    },
  },
  plugins: [],
}

