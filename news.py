"""Google News miniScraper"""
from urllib.request import urlopen
from bs4 import BeautifulSoup as web

HTML = urlopen("https://news.google.com")

BASE = web(HTML, "lxml")\
    .find("div", {"class":"section top-stories-section section-toptop"})

NEWS = BASE.findAll("h2", {"class":"esc-lead-article-title"})
SUMMARY = BASE.findAll("div", {"class":"esc-lead-snippet-wrapper"})

print("Here's some top stories to kickstart your day!", end="\n\n")
print("HEADLINES:")

for headline, description in zip(NEWS, SUMMARY):
    print(headline.get_text())
    print("-->", description.get_text(), end="\n\n")
