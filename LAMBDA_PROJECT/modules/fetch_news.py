import requests

from modules.config import NEWS_URL


def fetch_news():

    response = requests.get(NEWS_URL)

    response.raise_for_status()

    news_data = response.json()

    return news_data