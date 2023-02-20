from bs4 import BeautifulSoup
from selenium import webdriver
import random

driver = webdriver.Chrome()
driver.get("http://www.delfi.lt")
html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
titles = soup.select('.CBarticleTitle')

titles_with = []
titles_without = []
for title in titles:
    if ":" in title.get_text():
        titles_with.append(title.get_text()[:title.get_text().index(":")])
        titles_without.append(title.get_text()[title.get_text().index(":"):])

random.shuffle(titles_without)
for index,title in enumerate(titles_with):
    print(title + titles_without[index])



