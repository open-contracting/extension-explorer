try {
  Typekit.load({ async: true });
} catch (_e) {}

document.addEventListener("DOMContentLoaded", () => {
  // extensions.html
  const selects = document.querySelectorAll(".filter-select");
  if (selects.length) {
    const filters = {};

    selects.forEach((select) => {
      select.addEventListener("change", function () {
        filters[this.id] = this.value;
        const selector = Object.values(filters).join("");

        document.querySelectorAll(`.extension${selector}`).forEach((el) => {
          el.style.display = "";
        });
        if (selector) {
          document.querySelectorAll(`.extension:not(${selector})`).forEach((el) => {
            el.style.display = "none";
          });
        }

        document.getElementById("filter-count").textContent = selected.length;
      });
    });
  }

  // layout_extension.html
  const version = document.getElementById("version");
  if (version) {
    version.addEventListener("change", (event) => {
      window.location.href = event.target.value;
    });
  }

  if (typeof ClipboardJS !== "undefined" && document.querySelectorAll(".clipboard").length) {
    const clipboard = new ClipboardJS(".clipboard");

    clipboard.on("success", (event) => {
      const original = event.trigger.getAttribute("data-bs-original-title");
      const updated = event.trigger.getAttribute("data-updated-title");

      event.trigger.setAttribute("data-bs-original-title", updated);
      const tooltip = bootstrap.Tooltip.getInstance(event.trigger);
      if (tooltip) {
        tooltip.show();
      }
      event.trigger.setAttribute("data-bs-original-title", original);
      event.clearSelection();
    });

    document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach((el) => {
      new bootstrap.Tooltip(el);
    });
  }
});
