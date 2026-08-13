const base = require("./pa11y.default.js");

const knownWarnings = [
  {
    // "Elements must meet minimum color contrast ratio thresholds."
    // The contrast can't be determined, because the text overflows its container.
    rules: ["color-contrast"],
    selectors: [".ee-max-width pre code", "div.highlight pre span"],
  },
  {
    // "Accessible name for this element does not contain the visible label text."
    // The label is an icon, not text.
    // https://www.w3.org/WAI/WCAG21/Techniques/failures/F96
    rules: ["WCAG2AA.Principle2.Guideline2_5.2_5_3.F96"],
    selectors: ["button.ee-search-docs-toggle"],
  },
];

module.exports = {
  ...base,
  defaults: {
    ...base.createDefaults(knownWarnings),
    viewport: {
      width: 320,
      height: 480,
      deviceScaleFactor: 2,
      isMobile: true,
    },
  },
};
