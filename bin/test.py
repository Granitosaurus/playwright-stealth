import asyncio
from itertools import product

from playwright import async_playwright

from playwright_stealth.stealth import stealth_async


async def capture(pw, name, url, use_stealth=False, headless=False, browser='chromium'):
    print(f'crawling {url} with {browser}, head:{headless}, stealth: {use_stealth}')
    browser = await getattr(pw, browser).launch(headless=headless)
    page = await browser.newPage()
    if use_stealth:
        await stealth_async(page)
    await page.goto(url)
    await page.screenshot(path=f'{name}.png', fullPage=True)


async def main():
    urls = [
        ('sannysoft', 'https://bot.sannysoft.com/'),
        ('areuhead', 'http://arh.antoinevastel.com/bots/areyouheadless')
    ]
    # mix browser_type, use_head, use_stealth — all combinations
    mix = product(('chromium', 'firefox'), (True, False), (True, False), urls)
    async with async_playwright() as pw:
        for browser, use_head, use_stealth, url in mix:
            url_name, url = url
            await capture(
                pw,
                f'results/{browser}_head{"full" if use_head else "less"}_{"stealth_" if use_stealth else ""}{url_name}',
                use_stealth=use_stealth,
                headless=use_head,
                url=url
            )


if __name__ == '__main__':
    asyncio.run(main())
