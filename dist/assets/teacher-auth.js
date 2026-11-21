/* A browser-only deterrent for the static teacher resources. */
'use strict';
(() => {
  const passwordHash = 'a319b07f627c969fd67f535f4d921cae786374b101c3f1ec58c38f1b8eccfc19';
  const storageKey = 'painting-room:teacher:v1';
  const gates = [...document.querySelectorAll('.teacher-gate')];
  const content = [...document.querySelectorAll('[data-teacher-content]')];
  if (!gates.length) return;

  // SHA-256 in plain JavaScript also works offline and on HTTP school servers.
  function sha256(value) {
    const constants = [
      0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
      0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
      0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
      0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
      0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
      0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
      0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
      0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
    ];
    const bytes = new TextEncoder().encode(value);
    const buffer = new ArrayBuffer(Math.ceil((bytes.length + 9) / 64) * 64);
    const padded = new Uint8Array(buffer);
    padded.set(bytes);
    padded[bytes.length] = 0x80;
    const view = new DataView(buffer);
    view.setUint32(buffer.byteLength - 8, Math.floor(bytes.length / 0x20000000));
    view.setUint32(buffer.byteLength - 4, bytes.length * 8);
    const hash = [0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];
    const rotate = (n, bits) => (n >>> bits) | (n << (32 - bits));
    const words = new Uint32Array(64);
    for (let offset = 0; offset < buffer.byteLength; offset += 64) {
      for (let i = 0; i < 16; i++) words[i] = view.getUint32(offset + i * 4);
      for (let i = 16; i < 64; i++) {
        const x = words[i - 15], y = words[i - 2];
        words[i] = words[i - 16] + (rotate(x, 7) ^ rotate(x, 18) ^ (x >>> 3)) + words[i - 7] + (rotate(y, 17) ^ rotate(y, 19) ^ (y >>> 10));
      }
      let [a,b,c,d,e,f,g,h] = hash;
      for (let i = 0; i < 64; i++) {
        const t1 = (h + (rotate(e, 6) ^ rotate(e, 11) ^ rotate(e, 25)) + ((e & f) ^ (~e & g)) + constants[i] + words[i]) | 0;
        const t2 = ((rotate(a, 2) ^ rotate(a, 13) ^ rotate(a, 22)) + ((a & b) ^ (a & c) ^ (b & c))) | 0;
        h = g; g = f; f = e; e = (d + t1) | 0; d = c; c = b; b = a; a = (t1 + t2) | 0;
      }
      [a,b,c,d,e,f,g,h].forEach((word, i) => { hash[i] = (hash[i] + word) | 0; });
    }
    return hash.map(word => (word >>> 0).toString(16).padStart(8, '0')).join('');
  }

  let unlocked = false;
  let storageAvailable = true;
  function restore() {
    try { unlocked = sessionStorage.getItem(storageKey) === passwordHash; }
    catch (_) { storageAvailable = false; }
  }
  function render() {
    gates.forEach(gate => { gate.hidden = unlocked; });
    content.forEach(section => { section.hidden = !unlocked; });
    document.querySelectorAll('[data-teacher-print]').forEach(control => { control.hidden = !unlocked; });
    document.querySelectorAll('[data-teacher-session-status]').forEach(status => {
      status.textContent = storageAvailable ? 'Teacher access is unlocked for this tab.' : 'Teacher access is unlocked for this page. Browser storage is unavailable, so other pages will ask again.';
    });
    if (!unlocked) {
      document.body.classList.remove('print-teacher');
      const include = document.querySelector('#include-teacher');
      if (include) include.checked = false;
    }
  }
  gates.forEach(gate => {
    const form = gate.querySelector('form');
    const input = form.querySelector('input');
    const error = gate.querySelector('[role="status"]');
    form.hidden = false;
    input.addEventListener('input', () => { input.removeAttribute('aria-invalid'); error.textContent = ''; });
    form.addEventListener('submit', event => {
      event.preventDefault();
      if (sha256(input.value) !== passwordHash) {
        error.textContent = 'That password isn’t correct. Please try again.';
        input.setAttribute('aria-invalid', 'true');
        input.focus();
        input.select();
        return;
      }
      unlocked = true;
      input.value = '';
      input.removeAttribute('aria-invalid');
      error.textContent = '';
      try { sessionStorage.setItem(storageKey, passwordHash); }
      catch (_) { storageAvailable = false; }
      render();
      const heading = content[0].querySelector('h1, h2, h3');
      if (heading) { heading.tabIndex = -1; heading.focus({ preventScroll: true }); }
      const target = document.getElementById(location.hash.slice(1));
      if (target) target.scrollIntoView();
    });
  });
  document.querySelectorAll('[data-teacher-lock]').forEach(button => {
    button.addEventListener('click', () => {
      unlocked = false;
      try { sessionStorage.removeItem(storageKey); }
      catch (_) { storageAvailable = false; }
      render();
      gates[0].querySelector('input').focus();
    });
  });
  restore();
  render();
  window.addEventListener('pageshow', () => { restore(); render(); });
})();
