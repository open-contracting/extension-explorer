try {
  Typekit.load({ async: true });
} catch (_e) {}

$(() => {
  // extensions.html
  if ($(".filter-select").length) {
    const filters = {};

    $(".filter-select").on("change", function () {
      let prop,
        selector = "",
        selected;

      filters[this.id] = this.value;
      for (prop in filters) {
        selector += filters[prop];
      }

      selected = $(`.extension${selector}`).show();
      if (selector) {
        $(`.extension:not(${selector})`).hide();
      }

      $("#filter-count").text(selected.length);
    });
  }

  // layout_extension.html
  $("#version").on("change", function () {
    window.location.href = this.value;
  });

  if (typeof ClipboardJS !== "undefined" && $(".clipboard").length) {
    const clipboard = new ClipboardJS(".clipboard");

    clipboard.on("success", (e) => {
      const $trigger = $(e.trigger);
      const original = $trigger.data("bs-original-title");
      const updated = $trigger.data("updated-title");

      $trigger.attr("data-bs-original-title", updated).tooltip("show").attr("data-bs-original-title", original);
      e.clearSelection();
    });

    $('[data-toggle="tooltip"]').tooltip();
  }
});
