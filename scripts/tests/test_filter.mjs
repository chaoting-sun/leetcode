// Drives the real overrides/javascripts/filter.js against a minimal DOM mock
// to verify the filtering logic (F1: tag AND, difficulty, title search, count).
// No browser / jsdom: a hand-rolled mock is enough for this small surface.
//
//   node scripts/tests/test_filter.mjs

import fs from "node:fs";
import vm from "node:vm";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const code = fs.readFileSync(
  path.join(here, "../../overrides/javascripts/filter.js"),
  "utf8",
);

// ---- minimal DOM mock ----------------------------------------------------
function classList() {
  const s = new Set();
  return { add: (c) => s.add(c), remove: (c) => s.delete(c), contains: (c) => s.has(c) };
}
function makeChip(tag) {
  let onClick = null;
  return {
    dataset: { tag },
    classList: classList(),
    setAttribute() {},
    addEventListener: (ev, h) => { if (ev === "click") onClick = h; },
    click() { onClick && onClick(); },
  };
}
function makeRow(tags, difficulty, title) {
  return {
    dataset: { tags, difficulty },
    hidden: false,
    querySelector: (sel) =>
      sel === "td:nth-child(2)" ? { textContent: title } : null,
  };
}
function makeInput() {
  let h = null;
  return { value: "", addEventListener: (_e, fn) => { h = fn; }, fire() { h && h(); } };
}

const rows = [
  makeRow("array hash-table", "easy", "Two Sum"),
  makeRow("linked-list", "medium", "Add Two Numbers"),
  makeRow("array sliding-window", "medium", "Longest Substring"),
  makeRow("array", "hard", "Median of Two Sorted Arrays"),
];
const chips = {
  array: makeChip("array"),
  "hash-table": makeChip("hash-table"),
  "sliding-window": makeChip("sliding-window"),
};
const diffSel = makeInput();
const search = makeInput();
const count = { textContent: "" };

const filterEl = {
  querySelectorAll: (sel) => (sel === ".lc-chip" ? Object.values(chips) : []),
  querySelector: (sel) =>
    ({ ".lc-diff": diffSel, ".lc-search": search, ".lc-count": count }[sel] || null),
};
const tableEl = { querySelectorAll: (sel) => (sel === "tbody tr" ? rows : []) };

let domLoaded = null;
const documentMock = {
  getElementById: (id) => (id === "lc-table" ? tableEl : null),
  querySelector: (sel) => (sel === ".lc-filter" ? filterEl : null),
  addEventListener: (ev, fn) => { if (ev === "DOMContentLoaded") domLoaded = fn; },
};

// document$ undefined -> filter.js registers DOMContentLoaded; fire it.
vm.runInNewContext(code, { document: documentMock, console });
domLoaded();

// ---- assertions ----------------------------------------------------------
const visible = () =>
  rows.filter((r) => !r.hidden).map((r) => r.querySelector("td:nth-child(2)").textContent);
const eq = (a, b) => JSON.stringify(a) === JSON.stringify(b);

let failed = 0;
let n = 0;
function check(name, cond) {
  n++;
  if (cond) console.log("  PASS  " + name);
  else { failed++; console.log("  FAIL  " + name + " -> " + JSON.stringify(visible())); }
}

check("initial: all shown + count", visible().length === 4 && count.textContent === "Showing 4 of 4");

diffSel.value = "medium"; diffSel.fire();
check("difficulty=medium", eq(visible(), ["Add Two Numbers", "Longest Substring"]));

diffSel.value = ""; diffSel.fire();
chips.array.click();
check("tag=array", eq(visible(), ["Two Sum", "Longest Substring", "Median of Two Sorted Arrays"]));

chips["sliding-window"].click();
check("array AND sliding-window", eq(visible(), ["Longest Substring"]));

chips["sliding-window"].click(); // toggle off
diffSel.value = "hard"; diffSel.fire();
check("array AND difficulty=hard", eq(visible(), ["Median of Two Sorted Arrays"]));

diffSel.value = ""; diffSel.fire();
chips.array.click(); // toggle off array
search.value = "two"; search.fire();
check("title search 'two'", eq(visible(), ["Two Sum", "Add Two Numbers", "Median of Two Sorted Arrays"]));

search.value = ""; search.fire();
check("cleared: all shown", visible().length === 4 && count.textContent === "Showing 4 of 4");

console.log(`\n${n - failed}/${n} passed.`);
process.exit(failed ? 1 : 0);
