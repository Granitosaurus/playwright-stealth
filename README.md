# Playwright-Stealth

Helper scripts for avoiding bot detection of [playwright-python] controlled browsers.

Usage:
```
from playwright_stealth import stealth_async

async with async_playwright() as pw:
    browser = await pw.chromium.launch(headless=True)
    page = await browser.newPage()
    await stealth_async(page)
    await page.goto('https://bot.sannysoft.com/')
    await page.screenshot(path='chrome_headless_stealth.png', fullPage=True)
```

For more see `/bin/test_chrome.py` and `/bin/test_firefox.py`
and original puppeteer repo: https://github.com/berstend/puppeteer-extra/tree/master/packages/puppeteer-extra-plugin-stealth