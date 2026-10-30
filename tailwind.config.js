// tailwind.config.js
module.exports = {
  content: [
    "./templates/**/*.html",       // tus templates Django
    "./tw_dev/**/*.js",            // scripts propios
    "./node_modules/flowbite/**/*.js" // componentes de Flowbite
  ],
  safelist: [
    'bg-blue-600',
    'bg-gray-500',
    'hover:bg-blue-700',
    'hover:bg-gray-700',
  ],
  plugins: [
    require("flowbite/plugin")
  ],
};