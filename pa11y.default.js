// In CI, PA11Y_INCLUDE_WARNINGS is set along with PA11Y_SUPPRESS_KNOWN_WARNINGS, to allow pa11y to pass.
// In development, set PA11Y_INCLUDE_WARNINGS only, to review warnings manually.
const includeWarnings = "PA11Y_INCLUDE_WARNINGS" in process.env;

// pa11y supports hiding elements or ignoring rules - but not ignoring rules for specific elements.
// So, in development, this configuration can be run using each strategy, to avoid shadowing issues.
const strategy = process.env.PA11Y_STRATEGY;

// Suppress false positive warnings.
const suppressKnownWarnings = "PA11Y_SUPPRESS_KNOWN_WARNINGS" in process.env;

const knownErrors = {
  // "This form does not contain a submit button."
  // https://www.w3.org/WAI/WCAG21/Techniques/html/H32
  rules: ["WCAG2AA.Principle3.Guideline3_2.3_2_2.H32.2"],
  selectors: ["h1+form.form-inline", "form.ee-search"],
};

const knownWarnings = [
  {
    // "This element's text or background contains transparency."
    // https://www.w3.org/WAI/WCAG21/Techniques/general/G18
    rules: ["WCAG2AA.Principle1.Guideline1_4.1_4_3.G18.Alpha"],
    selectors: ["a.nav-link", ".text-body-secondary", "span.visually-hidden"],
  },
  {
    // "This element's text is placed on a background image."
    // https://www.w3.org/WAI/WCAG21/Techniques/general/G18
    rules: ["WCAG2AA.Principle1.Guideline1_4.1_4_3.G18.BgImage", "color-contrast"],
    selectors: ["select.form-select"],
  },
  {
    // "This element is absolutely positioned and the background color can not be determined."
    // https://www.w3.org/WAI/WCAG21/Techniques/general/G18
    rules: ["WCAG2AA.Principle1.Guideline1_4.1_4_3.G18.Abs"],
    selectors: ["span.visually-hidden"],
  },
  {
    // "If this table is a data table, consider using a caption element to the table element to identify this table."
    // https://www.w3.org/WAI/WCAG21/Techniques/html/H39
    rules: ["WCAG2AA.Principle1.Guideline1_3.1_3_1.H39.3.NoCaption"],
    selectors: [".ee-content table"],
  },
  {
    // "If this element contains a navigation section, it is recommended that it be marked up as a list."
    // https://www.w3.org/WAI/WCAG21/Techniques/html/H48
    rules: ["WCAG2AA.Principle1.Guideline1_3.1_3_1.H48"],
    selectors: [".ee-max-width p", ".ee-content p"],
  },
  {
    // "If this selection list contains groups of related options, they should be grouped with optgroup."
    // https://www.w3.org/WAI/WCAG21/Techniques/html/H85
    rules: ["WCAG2AA.Principle1.Guideline1_3.1_3_1.H85.2"],
    selectors: ["select#filter-core", "select#filter-publisher", "select#filter-profile"],
  },
  {
    // "This select element does not have a value available to an accessibility API."
    // https://www.w3.org/WAI/WCAG21/Techniques/html/H91
    rules: ["WCAG2AA.Principle4.Guideline4_1.4_1_2.H91.Select.Value"],
    selectors: ["select.filter-select"],
  },
  {
    // "Preformatted text may require scrolling in two dimensions."
    rules: ["WCAG2AA.Principle1.Guideline1_4.1_4_10.C32,C31,C33,C38,SCR34,G206"],
    selectors: [],
  },
];

const suppressions = [knownErrors, ...(includeWarnings && suppressKnownWarnings ? knownWarnings : [])];

// A suppression with no selector can't be hidden, so its rules are always ignored, regardless of strategy.
const withoutSelectors = suppressions.filter((suppression) => !suppression.selectors.length);
const withSelectors = suppressions.filter((suppression) => suppression.selectors.length);

const hideElements = strategy === "hideElements" ? withSelectors.flatMap((suppression) => suppression.selectors) : [];
const ignore = [
  ...withoutSelectors.flatMap((suppression) => suppression.rules),
  ...(strategy === "ignore" ? withSelectors.flatMap((suppression) => suppression.rules) : []),
];

module.exports = {
  defaults: {
    runners: ["htmlcs", "axe"],
    levelCapWhenNeedsReview: "warning",
    includeWarnings: includeWarnings,
    ...(hideElements.length ? { hideElements: hideElements.join(", ") } : {}),
    ...(ignore.length ? { ignore: ignore } : {}),
  },
  urls: [
    "http://127.0.0.1:8000/en/",
    "http://127.0.0.1:8000/es/",
    "http://127.0.0.1:8000/en/publishers/",
    "http://127.0.0.1:8000/es/publishers/",
    "http://127.0.0.1:8000/en/users/",
    "http://127.0.0.1:8000/es/users/",
    "http://127.0.0.1:8000/en/extensions/",
    "http://127.0.0.1:8000/es/extensions/",
    "http://127.0.0.1:8000/en/extensions/medicine/master/",
    "http://127.0.0.1:8000/es/extensions/medicine/master/",
    "http://127.0.0.1:8000/en/extensions/medicine/master/schema/",
    "http://127.0.0.1:8000/es/extensions/medicine/master/schema/",
    "http://127.0.0.1:8000/en/extensions/medicine/master/codelists/",
    "http://127.0.0.1:8000/es/extensions/medicine/master/codelists/",
  ],
};
