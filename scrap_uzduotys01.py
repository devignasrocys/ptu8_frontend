from bs4 import BeautifulSoup
from selenium import webdriver
import random

driver = webdriver.Chrome()
driver.get("http://www.delfi.lt")
html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
titles = soup.select('.CBarticleTitle')

titles_without = []
titles_with = []
bad_words = ["COVID", "mirtis", "skiepai"]
for title in titles:
    if ":" in title.get_text():
        if not any(word in title.get_text() for word in bad_words):
            titles_without.append(title.get_text()[:title.get_text().index(":")])
            titles_with.append(title.get_text()[title.get_text().index(":"):])

random.shuffle(titles_with)
for index,title in enumerate(titles_without):
    print(title + titles_with[index])



