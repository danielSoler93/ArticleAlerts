import requests
from scholarly import scholarly
from bs4 import BeautifulSoup
import re
from . import article as ar
from . import checker as ck
from stem import Signal
from stem.control import Controller
import requests
from stem.util.log import get_logger
logger = get_logger()
logger.propagate = False

URL ="https://scholar.google.es/scholar?start={}&q={}&hl=es&as_sdt=0,5&as_ylo={}"



class Scraper():

    def __init__(self, topic, year, limit=0):
        self.topic = topic
        self.year = year
        self.limit = limit
        self.url = self.get_url()


    def scrape(self):
        html = self.get_html()
        ck.Checker(html).check()
        articles = self.get_articles(html)
        return articles

    def get_html(self):
        with Controller.from_port(port=9051) as c:
            c.authenticate()
            c.signal(Signal.NEWNYM)
        session = self._get_tor_session()
        url = session.get(self.url)
        html = url.text
        return html

    def get_url(self):
        url_with_spaces = URL.format(self.limit, self.topic, self.year)
        url_without_spaces =  url_with_spaces.replace(" ", "+")
        print(f"Scraping URL {url_without_spaces} ...")
        return url_without_spaces


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
         abstract = article.find("div", class_="gs_rs")
         abstract = abstract.text if abstract else ""
         article = ar.Article(title.text, authors, title["href"],
                              year, abstract)
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