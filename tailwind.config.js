// tailwind.config.js
module.exports = {
  content: [
    "./templates/**/*.html",       // tus templates Django
    "./tw_dev/**/*.js",            // scripts propios
    "./node_modules/flowbite/**/*.js" // componentes de Flowbite
  ],
  plugins: [
    require("flowbite/plugin")
  ],
};