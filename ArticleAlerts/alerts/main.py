from datetime import datetime
import os
import time
from . import scrape as sc
from . import database as db

DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class AlertManager(sc.Scraper, db.DB):

    def __init__(self, topic):
        self.topic = topic
        self.year = datetime.now().year
        db.DB.__init__(self, self._get_database_name())
        sc.Scraper.__init__(self, self.topic, self.year)

    def check(self):
        articles = self.download(self.url)
        self.update(articles)

    def download(self, url):
        articles = []
        while not articles:
            articles = self.scrape()
            if not articles:
                time.sleep(10)
        return articles

    def _get_database_name(self):
        topic_without_spaces = self.topic.replace(" ", "_")
        db_name = os.path.join(DIR, "dbs", f'{topic_without_spaces}.csv')
        return db_name
