try {
  Typekit.load({ async: true });
} catch (e) {}

$(function () {
  // extensions.html
  if ($(".filter-select").length) {
    var filters = {};

    $(".filter-select").on("change", function () {
      var prop,
        selector = "",
        selected;

      filters[this.id] = this.value;
      for (prop in filters) {
        selector += filters[prop];
      }

      selected = $(".extension" + selector).show();
      if (selector) {
        $(".extension:not(" + selector + ")").hide();
      }

      $("#filter-count").text(selected.length);
    });
  }

  // layout_extension.html
  if (typeof ClipboardJS !== "undefined" && $(".clipboard").length) {
    var clipboard = new ClipboardJS(".clipboard");

    clipboard.on("success", function (e) {
      var $trigger = $(e.trigger);
      var original = $trigger.data("bs-original-title");
      var updated = $trigger.data("updated-title");

      $trigger.attr("data-bs-original-title", updated).tooltip("show").attr("data-bs-original-title", original);
      e.clearSelection();
    });

    $('[data-toggle="tooltip"]').tooltip();
  }
});
