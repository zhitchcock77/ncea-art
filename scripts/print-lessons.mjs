// Regenerate downloadable A4 lesson PDFs using the installed Chromium browser.
import { spawn } from 'node:child_process';
import { mkdtemp, mkdir, writeFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { resolve, join, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const profile = await mkdtemp(join(tmpdir(), 'painting-room-print-'));
const browser = spawn(process.env.CHROMIUM_BIN || 'chromium', [
  '--headless', '--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage',
  '--no-first-run', '--no-default-browser-check', '--remote-debugging-port=0',
  `--user-data-dir=${profile}`, 'about:blank'
], { stdio: ['ignore', 'ignore', 'pipe'] });
let socket;
try {
  const endpoint = await new Promise((accept, reject) => {
    let log = '';
    const timeout = setTimeout(() => reject(new Error('Chromium startup timed out')), 20000);
    browser.once('error', reject);
    browser.once('exit', code => reject(new Error(`Chromium exited before startup (${code})`)));
    browser.stderr.on('data', chunk => {
      log += chunk.toString();
      const match = log.match(/DevTools listening on (ws:\/\/\S+)/);
      if (match) { clearTimeout(timeout); accept(match[1]); }
    });
  });
  socket = new WebSocket(endpoint);
  await new Promise((accept, reject) => { socket.onopen = accept; socket.onerror = reject; });
  let nextId = 0;
  const pending = new Map();
  const browserErrors = [];
  socket.onmessage = ({ data }) => {
    const message = JSON.parse(data);
    if (message.method === 'Runtime.exceptionThrown') browserErrors.push(message.params.exceptionDetails.text);
    if (!message.id) return;
    const handler = pending.get(message.id);
    if (!handler) return;
    pending.delete(message.id);
    clearTimeout(handler.timeout);
    if (message.error) handler.reject(new Error(message.error.message));
    else handler.accept(message.result);
  };
  function call(method, params = {}, sessionId) {
    return new Promise((accept, reject) => {
      const id = ++nextId;
      const timeout = setTimeout(() => { pending.delete(id); reject(new Error(`${method} timed out`)); }, 30000);
      pending.set(id, { accept, reject, timeout });
      socket.send(JSON.stringify({ id, method, params, ...(sessionId ? { sessionId } : {}) }));
    });
  }
  const { targetId } = await call('Target.createTarget', { url: 'about:blank' });
  const { sessionId } = await call('Target.attachToTarget', { targetId, flatten: true });
  const command = (method, params) => call(method, params, sessionId);
  await command('Page.enable');
  await command('Runtime.enable');
  async function evaluate(expression) {
    const result = await command('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true });
    if (result.exceptionDetails) throw new Error(result.exceptionDetails.text);
    return result.result.value;
  }
  async function navigate(file) {
    const url = pathToFileURL(join(root, 'dist', file)).href;
    await command('Page.navigate', { url });
    for (let attempt = 0; attempt < 100; attempt++) {
      if (await evaluate(`location.href === ${JSON.stringify(url)} && document.readyState === 'complete'`)) break;
      await new Promise(accept => setTimeout(accept, 50));
      if (attempt === 99) throw new Error(`Page did not load: ${file}`);
    }
    await evaluate('document.fonts.ready.then(() => true)');
  }
  await mkdir(join(root, 'dist', 'print'), { recursive: true });
  const files = [ ['lessons-1-2.html', 'lessons-1-2.pdf'], ...Array.from({ length: 12 }, (_, i) => {
    const slug = `lesson-1-2-${String(i + 1).padStart(2, '0')}`;
    return [`${slug}.html`, `${slug}.pdf`];
  }) ];
  for (const [html, pdf] of files) {
    await navigate(html);
    const printed = await command('Page.printToPDF', { printBackground: false, displayHeaderFooter: false, preferCSSPageSize: true });
    await writeFile(join(root, 'dist', 'print', pdf), Buffer.from(printed.data, 'base64'));
    console.log(`Printed ${pdf}`);
  }
  if (process.argv.includes('--verify')) {
    for (const file of ['teacher.html', 'lessons-1-2.html', 'lesson-1-2-08.html', 'task-1-2.html']) {
      await navigate(file);
      for (const width of [1400, 390]) {
        await command('Emulation.setDeviceMetricsOverride', { width, height: 950, deviceScaleFactor: 1, mobile: false });
        const measure = await evaluate('({width:innerWidth,content:document.documentElement.scrollWidth})');
        if (measure.content > measure.width) throw new Error(`Horizontal overflow: ${file} at ${width}: ${JSON.stringify(measure)}`);
        if (file !== 'task-1-2.html') {
          const { data } = await command('Page.captureScreenshot', { format: 'png' });
          await writeFile(join(tmpdir(), `painting-room-${file.replace('.html','')}-${width}.png`), Buffer.from(data, 'base64'));
        }
      }
      if (file !== 'teacher.html') {
        const printed = await evaluate('(() => { let count=0; window.print=()=>{count++}; document.querySelector(".print-button").click(); return count; })()');
        if (printed !== 1) throw new Error(`Print control failed: ${file}`);
      }
    }
    if (browserErrors.length) throw new Error(`Browser errors: ${browserErrors.join(', ')}`);
    console.log('Verified desktop/mobile widths, print controls and browser errors. Screenshots saved in the system temporary directory.');
  }
} finally {
  socket?.close();
  browser.kill('SIGTERM');
  await new Promise(accept => { if (browser.exitCode !== null) accept(); else browser.once('exit', accept); });
  await rm(profile, { recursive: true, force: true, maxRetries: 3 });
}
