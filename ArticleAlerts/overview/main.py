import ArticleAlerts.alerts.scrape as sc
import ArticleAlerts.overview.analysis as an
import numpy as np
import time

def retrieve_articles(alert, year, limit):
    pages = np.arange(0, limit, 10).tolist()
    for page in pages:
        found = False
        while not found:
            articles = sc.Scraper(alert, year, page).scrape()
            found = True if articles else False
            time.sleep(10)
        yield articles

def main(alert, topics, year=2020, limit=100):
    analysis_title = an.Analyser()
    for articles in retrieve_articles(alert, year, limit):
        titles = [article.title.lower() for article in articles]
        analysis_title.analyse(titles, topics)
    analysis_title.plot()




if __name__ == "__main__":
    topics = ["source",
              "machine learning",
              "ML",
              "DL",
              "AI"]
    main("drug discovery", topics, 2020, 10)
