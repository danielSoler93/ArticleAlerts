from datetime import datetime
import os
import time
from . import scrape as sc
from . import database as db

URL = "https://scholar.google.es/scholar?as_ylo={}&q={}&hl=es&as_sdt=0,5"
DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class AlertManager(sc.Scraper, db.DB):

    def __init__(self, topic):
        self.topic = topic
        self.year = datetime.now().year
        db.DB.__init__(self, self._get_database_name())


    def check(self):
        url = self.get_url()
        articles = self.download(url)
        self.update(articles)

    def download(self, url):
        articles = []
        while not articles:
            sc.Scraper.__init__(self, url)
            articles = self.scrape()
            if not articles:
                time.sleep(10)
        return articles

    def get_url(self):
        url_with_spaces = URL.format(self.year, self.topic)
        url_without_spaces =  url_with_spaces.replace(" ", "+")
        print(f"Scraping URL {url_without_spaces} ...")
        return url_without_spaces

    def _get_database_name(self):
        topic_without_spaces = self.topic.replace(" ", "_")
        db_name = os.path.join(DIR, "dbs", f'{topic_without_spaces}.csv')
        return db_name
