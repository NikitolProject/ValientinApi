import re
import requests

from bs4 import BeautifulSoup


async def parser(url):
  soup = BeautifulSoup(requests.get(url).content)
  test = soup.select("img.t0fcAb")
  return [i['src'] for i in test]
