import subprocess
import os
from . import scihub
import threading
import multiprocessing

DIR= os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(DIR))
ARTICLES_FOLDER = os.path.join(ROOT_DIR, "articles")

class ArticleDownloader:

    def  __init__(self, article_url, output_folder="."):
        self.article_url = article_url
        self.output = os.path.join(ARTICLES_FOLDER, output_folder.rsplit(".")[0])

    def download(self):
        if not os.path.exists(self.output):
            os.makedirs(self.output)
        scipy = os.path.join(DIR, "scihub.py")
        cmd = f"python {scipy} -d {self.article_url} --output {self.output}"
        subprocess.Popen(cmd.split())
