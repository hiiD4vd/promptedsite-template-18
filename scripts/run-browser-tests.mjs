import {spawn} from 'node:child_process';
import {chromium} from '@playwright/test';
import assert from 'node:assert/strict';
const base='http://127.0.0.1:4328';const server=spawn(process.execPath,['scripts/serve.mjs','dist','4328'],{stdio:'ignore'});
let browser;
try{
 for(let attempt=0;attempt<50;attempt++){if(await fetch(base).then(r=>r.ok,()=>false))break;await new Promise(r=>setTimeout(r,100));}
 browser=await chromium.launch({channel:process.env.BROWSER_CHANNEL||'chrome',headless:true});
 for(const width of [1440,390]){
 const page=await browser.newPage({viewport:{width,height:900},reducedMotion:'reduce'});const errors=[],failed=[];
 page.on('pageerror',e=>errors.push(e.message));page.on('response',r=>{if(r.status()>=400)failed.push(r.url())});
 await page.route('**/*',r=>r.request().url().startsWith('http')&&!r.request().url().startsWith(base)?r.abort():r.continue());
 await page.goto(base+'/?autoplay=0',{waitUntil:'domcontentloaded'});await page.getByRole('button',{name:/^start$/i}).waitFor({state:'visible',timeout:60000});
 assert.equal(await page.getByRole('button',{name:/^start$/i}).evaluate(el=>getComputedStyle(el).cursor),'pointer');
 await page.getByRole('button',{name:/^start$/i}).click({timeout:60000});
 assert.equal(await page.locator('body').evaluate(el=>[el,...el.querySelectorAll('*')].some(node=>getComputedStyle(node).cursor==='none')),false);
 for(let i=0;i<3;i++){await page.locator('.button-controls').nth(1).click();await page.waitForTimeout(1700);}
 if(width===390){await page.getByRole('button',{name:'Open menu'}).click();await page.keyboard.press('Escape');await page.getByRole('button',{name:'Open menu'}).waitFor();}
 await page.locator('#locations').scrollIntoViewIfNeeded();await page.locator('.map-marker__button').first().click();await page.getByRole('dialog').waitFor();await page.keyboard.press('Escape');assert.equal(await page.getByRole('dialog').count(),0);
 assert.deepEqual(errors,[]);assert.deepEqual(failed,[]);assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1),false);
 await page.close();console.log(`Passed offline browser checks at ${width}px`);
 }
}finally{await browser?.close();server.kill();}
