/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./node_modules/flowbite/**/*.css",
    "./node_modules/flowbite/**/*.js",
    "./src/**/*.{html,js}"
  ],
  theme: {
    extend: {
      container: {
        center: true,
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}