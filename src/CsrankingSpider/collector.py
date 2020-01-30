import aiohttp
import requests
from urllib.parse import urlparse

from ..CsrankingSpider.processor import extract_professor_information, extract_page_text

timeout = aiohttp.ClientTimeout(total=20)
session = aiohttp.ClientSession(timeout=timeout)

cs_ranking_url = 'http://csrankings.org/csrankings.csv'


async def get(url):
    """
    send get request
    :param url: the target url
    :return: the result text
    """

    async with session.get(url, headers=get_header(url)) as response:
        result = await response.text()
        return result


async def fetch_cs_ranking() -> str:
    """
    fetch professors of cs ranking.
    """
    csv_text = requests.get(cs_ranking_url, headers=get_header(cs_ranking_url)).text

    return csv_text


async def close_session():
    await session.close()


def get_header(url):
    cooked_url = urlparse(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Cache-Control': 'no-cache',
        'Accept-Language': 'en-US,en;q=0.5',
        'Host': cooked_url.hostname
    }
    return headers


async def get_all_professor_information_from_network():
    print("fetching all professor index url")
    professor_data = await fetch_cs_ranking()
    print("finish fetching")
    return extract_professor_information(professor_data)


async def get_all_professor_information_from_file(filename):
    print('Reading page list from file.')
    file = open(filename)
    return extract_professor_information(file.read())


async def get_professor_indexes(info):
    if len(info) < 3:
        return

    url = info[2]

    if url == '':
        return

    print(f'fetching index of {info[0]}')
    page = await get(url)
    text = extract_page_text(page)
    print(f'finish fetching index of {info[0]}')
    return text
