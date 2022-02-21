import pytest
from tests.utils import run_and_eval

from playwright_stealth.stealth import StealthConfig

@pytest.mark.asyncio
async def test_navigator_webdriver():
    # no stealth
    assert await run_and_eval('navigator.webdriver') is True
    # default
    conf = StealthConfig()
    assert await run_and_eval('navigator.webdriver', conf) is None
    # disable
    conf.webdrive = False
    assert await run_and_eval('navigator.webdriver') is True
