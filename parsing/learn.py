import requests
from bs4 import BeautifulStoneSoup as BS

r = requests.get("https://stopgame.ru/review/p1?subsection=izumitelno")
html = BS(r.content, 'html.parser')

for el in html.select("143411"):
    title = el.select('.caption > a')
    print(title[0].text)
