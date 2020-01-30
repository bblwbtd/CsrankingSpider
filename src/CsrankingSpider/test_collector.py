import asyncio
from unittest import TestCase

import aiohttp

from src.CsrankingSpider.collector import get


class TestCollector(TestCase):
    loop = asyncio.get_event_loop()
    session = aiohttp.ClientSession()

    def test_get(self):
        text = self.loop.run_until_complete(get(self.session, 'http://www.baidu.com/'))
        print(text)
