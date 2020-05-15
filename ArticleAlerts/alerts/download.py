import subprocess
import os
from . import scihub
import threading
import multiprocessing

DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARTICLES_FOLDER = os.path.join(DIR, "articles")

class ArticleDownloader:

    def  __init__(self, article_url, output_folder="."):
        self.article_url = article_url
        self.output = os.path.join(ARTICLES_FOLDER, output_folder.rsplit(".")[0])

    def download(self):
        if not os.path.exists(self.output):
            os.makedirs(self.output)
        try:
            multiprocessing.Process(target=scihub.main, args=(self.article_url,), kwargs={'output': self.output}).start()
        except Exception:
            pass
