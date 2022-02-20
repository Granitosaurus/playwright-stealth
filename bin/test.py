import asyncio
from itertools import product

from playwright.async_api import async_playwright, Page

from playwright_stealth.stealth import stealth_async


async def capture(pw, name, url, use_stealth=False, headless=False, browser="chromium"):
    print(f"crawling {url} with {browser}, head:{headless}, stealth: {use_stealth}")
    browser = await getattr(pw, browser).launch(headless=headless)
    page: Page = await browser.new_page()
    if use_stealth:
        await stealth_async(page)
    await page.goto(url)
    await page.screenshot(path=f"{name}.png", full_page=True)
    await page.close()


async def main():
    urls = [
        ("sannysoft", "https://bot.sannysoft.com/"),
        # ('areuhead', 'http://arh.antoinevastel.com/bots/areyouheadless')
    ]
    # mix browser_type, use_head, use_stealth — all combinations
    mix = product(
        ("chromium", "firefox"),  # browser type
        (True, False),  # to use headless mode or not
        (True, False),  # to use stealth or not
        urls
    )
    mix = (('chromium', True, True, urls[0]),)
    async with async_playwright() as pw:
        for browser, use_head, use_stealth, url in mix:
            url_name, url = url
            await capture(
                pw,
                f'results/{browser}_head{"less" if use_head else "full"}_{"stealth_" if use_stealth else ""}{url_name}',
                use_stealth=use_stealth,
                headless=use_head,
                url=url,
            )


if __name__ == "__main__":
    asyncio.run(main())
