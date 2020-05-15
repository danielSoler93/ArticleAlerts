import subprocess
import os

DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARTICLES_FOLDER = os.path.join(DIR, "articles")

class ArticleDownloader:

    def  __init__(self, article_url, output_folder="."):
        self.article_url = article_url
        self.output = os.path.join(ARTICLES_FOLDER, output_folder)

    def download(self):
        if not os.path.exists(self.output):
            os.makedirs(self.output)
        cmd = f"python /Users/nostrum/repos/scihub.py/scihub/scihub.py -d {self.article_url} --output {self.output}"
        subprocess.Popen(cmd.split())
