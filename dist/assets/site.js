'use strict';
document.documentElement.classList.add('js');
const search = document.querySelector('#task-search');
if (search) {
  const select = document.querySelector('#level-filter');
  const rows = [...document.querySelectorAll('.task-table tbody tr')];
  const count = document.querySelector('#filter-count');
  function filter() {
    const query = search.value.toLocaleLowerCase('en-NZ').trim();
    let shown = 0;
    for (const row of rows) {
      const matches = (select.value === 'all' || row.dataset.level === select.value) && row.dataset.search.includes(query);
      row.hidden = !matches;
      if (matches) shown++;
    }
    count.textContent = `${shown} task sheet${shown === 1 ? '' : 's'}`;
    document.querySelector('#no-results').hidden = shown !== 0;
  }
  search.addEventListener('input', filter);
  select.addEventListener('change', filter);
  document.querySelector('.filters').addEventListener('submit', event => event.preventDefault());
  document.querySelector('#reset-filters').addEventListener('click', () => {
    search.value = ''; select.value = 'all'; filter(); search.focus();
  });
}
const sheet = document.querySelector('[data-sheet]');
if (sheet) {
  const key = `painting-room:v1:${sheet.dataset.sheet}`;
  const fields = [...sheet.querySelectorAll('[data-save]')];
  const status = document.querySelector('#storage-status');
  function progress() {
    const checks = fields.filter(f => f.type === 'checkbox');
    document.querySelector('.check-progress').textContent = `${checks.filter(f => f.checked).length} of ${checks.length} evidence checks complete`;
  }
  function storageError() {
    status.textContent = 'Browser storage is unavailable. You can still use this sheet; print or copy your notes before leaving.';
  }
  try {
    const raw = localStorage.getItem(key);
    const saved = raw ? JSON.parse(raw) : {};
    if (saved && typeof saved === 'object' && !Array.isArray(saved)) {
      fields.forEach(field => {
        const val = saved[field.dataset.save];
        if (field.type === 'checkbox' && typeof val === 'boolean') field.checked = val;
        else if (typeof val === 'string') field.value = val;
      });
    }
    status.textContent = raw ? 'Working notes restored from this browser. This website does not submit assessment evidence.' : 'Working notes stay in this browser when storage is available. This website does not submit assessment evidence.';
  } catch (_) { storageError(); }
  progress();
  function save() {
    const data = {};
    fields.forEach(f => { data[f.dataset.save] = f.type === 'checkbox' ? f.checked : f.value; });
    progress();
    try { localStorage.setItem(key, JSON.stringify(data)); status.textContent = 'Working notes saved in this browser. This website does not submit assessment evidence.'; }
    catch (_) { storageError(); }
  }
  fields.forEach(f => f.addEventListener(f.type === 'checkbox' ? 'change' : 'input', save));
  document.querySelector('.clear-notes').addEventListener('click', () => {
    fields.forEach(f => { if (f.type === 'checkbox') f.checked = false; else f.value = ''; });
    try { localStorage.removeItem(key); status.textContent = 'This sheet’s working notes and checks have been cleared.'; }
    catch (_) { storageError(); }
    progress();
  });
  document.querySelector('#include-teacher').addEventListener('change', event => {
    document.body.classList.toggle('print-teacher', event.target.checked);
  });
  let wasOpen = true;
  window.addEventListener('beforeprint', () => {
    const details = document.querySelector('.teacher-notes details');
    wasOpen = details.open; details.open = true;
    fields.filter(f => f.tagName === 'TEXTAREA').forEach(f => {
      f.style.height = 'auto'; f.style.height = `${f.scrollHeight + 8}px`;
    });
  });
  window.addEventListener('afterprint', () => {
    document.querySelector('.teacher-notes details').open = wasOpen;
    fields.filter(f => f.tagName === 'TEXTAREA').forEach(f => { f.style.height = ''; });
  });
}
document.querySelectorAll('.print-button').forEach(button => {
  button.addEventListener('click', () => window.print());
});
