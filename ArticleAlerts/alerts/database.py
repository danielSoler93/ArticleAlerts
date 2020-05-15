import pandas as pd
import os
from . import article as ar
from . import download as dw

class DB():

    def __init__(self, db):
        self.db_absolute_path = db
        self.db_name = os.path.basename(db)
        self.db = self._retrieve_db(db)


    def update(self, articles):
        old_articles = self.pull_articles_from_db()
        for article in articles:
            if article.title not in old_articles:
                print(f"New article {article.title} in {self.db_name}")
                self.db = self.push_article_to_db(article)
                dw.ArticleDownloader(article.link, self.db_name).download()
        self.dump_db()

    def pull_articles_from_db(self):
        try:
            return self.db["title"].values
        except KeyError: #If empty
            return []

    def push_article_to_db(self, article: ar.Article):
        return self.db.append(article.__dict__, ignore_index=True)

    def dump_db(self,  filename=None, output_folder="."):
        filename = filename if filename else self.db_absolute_path
        file = os.path.join(output_folder, filename)
        self.db.to_csv(file, index=False)

    def _retrieve_db(self, db):
        if os.path.exists(db):
            df=pd.read_csv(db, index_col=False)
        else:
            df=pd.DataFrame()
        return df





