import requests

import config


class Parser:

    @classmethod
    def parse_article(cls, article):
        params = (
            ('locale', 'ru'),
            ('lang', 'ru'),
            ('nm', article)
        )
        response = requests.get(config.URL, headers=config.HEADERS, params=params)
        return response.json()
