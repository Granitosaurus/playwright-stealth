from typing import Optional

from playwright.async_api import async_playwright, Page

from playwright_stealth.stealth import StealthConfig, stealth_async

async def run_and_eval(script, stealth_conf: Optional[StealthConfig]=None):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        page: Page = await browser.new_page()
        if stealth_conf:
            await stealth_async(page, stealth_conf)
        await page.goto('http://httpbin.org/html')
        return await page.evaluate(script)

