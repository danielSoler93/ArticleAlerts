import requests
from scholarly import scholarly
from bs4 import BeautifulSoup
import re
from . import article as ar
from . import checker as ck

import requests





class Scraper():

    def __init__(self, url):
        self.url = url

    def scrape(self):
        html = self.get_html()
        ck.Checker(html).check()
        articles = self.get_articles(html)
        return articles

    def get_html(self):
        session = self._get_tor_session()
        url = session.get(self.url)
        html = url.text
        return html

    def get_articles(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        articles = soup.find_all("div", class_="gs_ri")
        articles = [self._get_title(article) for article in articles]
        return articles

    def _get_title(self, article):
         title = article.find("h3", class_="gs_rt").find("a")
         authors = ",".join([author.text for author in article.find("div", class_="gs_a").find_all("a")])
         date = article.find("div", class_="gs_a").text
         match = re.search('\d{4}', date)
         year = match.group(0)
         article = ar.Article(title.text, authors, title["href"], year)
         return article

    def _get_tor_session(self):
        session = requests.session()
        # Tor uses the 9050 port as the default socks port
        session.proxies = {'http': 'socks5://127.0.0.1:9050',
                           'https': 'socks5://127.0.0.1:9050'}
        return session

class ApiScraper:


    def __init__(self, topic):
        self.topic = topic
        proxies = {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'}
        scholarly.use_proxy(**proxies)

    def search(self):
        search_query = scholarly.search_pubs_query(self.topic)
        print(next(search_query))