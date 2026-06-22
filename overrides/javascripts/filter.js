// Client-side filtering for the Problems page (F1): multi-select tag chips
// (AND), a difficulty dropdown, and a title search box, combined with AND.
// Re-initialized on every (instant) navigation via Material's document$.

function initLcFilter() {
  const table = document.getElementById("lc-table");
  const filter = document.querySelector(".lc-filter");
  if (!table || !filter) return; // not the Problems page

  const rows = Array.from(table.querySelectorAll("tbody tr"));
  const chips = Array.from(filter.querySelectorAll(".lc-chip"));
  const diffSel = filter.querySelector(".lc-diff");
  const search = filter.querySelector(".lc-search");
  const count = filter.querySelector(".lc-count");

  const activeTags = new Set();

  function apply() {
    const diff = diffSel ? diffSel.value : "";
    const q = search ? search.value.trim().toLowerCase() : "";
    let shown = 0;
    for (const tr of rows) {
      const rowTags = (tr.dataset.tags || "").split(" ").filter(Boolean);
      const rowDiff = tr.dataset.difficulty || "";
      const titleCell = tr.querySelector("td:nth-child(2)");
      const title = (titleCell ? titleCell.textContent : "").toLowerCase();

      let ok = true;
      if (diff && rowDiff !== diff) ok = false;
      if (ok && activeTags.size) {
        for (const t of activeTags) {
          if (!rowTags.includes(t)) { ok = false; break; }
        }
      }
      if (ok && q && !title.includes(q)) ok = false;

      tr.hidden = !ok;
      if (ok) shown++;
    }
    if (count) count.textContent = `Showing ${shown} of ${rows.length}`;
  }

  for (const chip of chips) {
    chip.addEventListener("click", () => {
      const tag = chip.dataset.tag;
      if (activeTags.has(tag)) {
        activeTags.delete(tag);
        chip.classList.remove("lc-chip--active");
        chip.setAttribute("aria-pressed", "false");
      } else {
        activeTags.add(tag);
        chip.classList.add("lc-chip--active");
        chip.setAttribute("aria-pressed", "true");
      }
      apply();
    });
  }
  if (diffSel) diffSel.addEventListener("change", apply);
  if (search) search.addEventListener("input", apply);

  apply(); // set the initial "Showing N of M" count
}

// document$ is provided by Material for MkDocs and emits on initial load and
// after every instant navigation. Fall back to DOMContentLoaded otherwise.
if (typeof document$ !== "undefined") {
  document$.subscribe(initLcFilter);
} else {
  document.addEventListener("DOMContentLoaded", initLcFilter);
}
