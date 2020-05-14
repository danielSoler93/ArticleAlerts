import requests
from bs4 import BeautifulSoup
import re
from . import article as ar


class Scraper:

    def __init__(self, url):
        self.url = url

    def scrape(self):
        html = self.get_html()
        articles = self.get_articles(html)
        return articles

    def get_html(self):
        url = requests.get(self.url)
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

