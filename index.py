import urllib.request
from bs4 import BeautifulSoup
import csv
import pandas as pd

class Scraper:
    def __init__(self, site):
        self.site = site

    outfile = open("scrape.csv","w",newline='')
    writer = csv.writer(outfile)
    
    outfile.close()

    def scrape(self):
        
        df = pd.DataFrame(columns=['pagename','alt'])
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "articles" in url:
                print("\n" + url)
                df2 = pd.DataFrame([[url]],columns=['pagename'])
                df.to_csv('scrape.csv')

news = "https://news.google.com/"
Scraper(news).scrape()


