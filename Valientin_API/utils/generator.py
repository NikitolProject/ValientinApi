import requests
import urllib


async def generator(images: dict):
  return [str(urllib.request.urlopen(url).read()) for url in images]