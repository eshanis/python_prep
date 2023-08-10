from cachetools import cached, TTLCache
import requests

cache = TTLCache(maxsize=100, ttl=86400)

@cached(cache)
def extract_article_content(url):
    response = requests.get(url)
    content = response.content
    return content