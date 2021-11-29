import pytest
from web_crawler import WebSpider


class TesteWebCrawler:

    def setup(self):
        pass

    def teste_site(self):
        web = WebSpider()

        assert web.site("https://pt.wikipedia.org/wiki/Python") == True
