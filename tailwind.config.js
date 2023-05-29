/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        clifford: "#da373d"
      },
      backgroundImage: {
        "burger-menu": "url('./assets/img/berger-menu.svg')"
      },
      fontFamily: {
        "gt-super": ["gt-super"],
        "twk-lausanne": ["twk-lausanne"]
      }
    }
  },
  plugins: []
}
