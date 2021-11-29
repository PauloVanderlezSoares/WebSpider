from bs4 import BeautifulSoup
from requests import get
import html5lib
from web_crawler import WebSpider

link = "https://pt.wikipedia.org/wiki/Python"

web = WebSpider()
web.site(link)
web.title_page()

# Gera um arquivo txt
web.webcrawler()
