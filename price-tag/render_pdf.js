// HTML → A4 PDF (실치수, 여백 0, 배율 100%)
let chromium;
try { ({ chromium } = require('playwright')); }
catch { ({ chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright')); }
const path = require('path');

(async () => {
  const [src, out] = process.argv.slice(2);
  // 내려받은 인쇄 엔진이 없으면 PC에 설치된 Chrome / Edge 사용
  let browser;
  for (const opts of [{}, { channel: 'chrome' }, { channel: 'msedge' }]) {
    try { browser = await chromium.launch(opts); break; } catch (e) { if (!opts.channel) var firstErr = e; }
  }
  if (!browser) throw firstErr;
  const page = await browser.newPage();
  await page.goto(require('url').pathToFileURL(path.resolve(src)).href);
  await page.waitForFunction(() => document.body.dataset.fitted === '1');
  const warnings = await page.evaluate(() => [...document.querySelectorAll('.tag')]
    .filter(t => t.dataset.productClamped || t.dataset.memberOverflow)
    .map(t => ({ row: +t.dataset.row, productClamped: !!t.dataset.productClamped, memberOverflow: !!t.dataset.memberOverflow })));
  await page.emulateMedia({ media: 'print' });
  await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  await browser.close();
  const seen = new Set();
  process.stdout.write(JSON.stringify({ pdf: out, warnings: warnings.filter(w => !seen.has(w.row) && seen.add(w.row)) }));
})().catch(e => { console.error(e); process.exit(1); });
