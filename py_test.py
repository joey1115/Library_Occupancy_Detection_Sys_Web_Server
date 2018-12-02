import time
import random
import sqlite3
import bs4

with open("templates/index.html", "r") as inf:
    txt = inf.read()
    print(txt)
    soup = bs4.BeautifulSoup(txt, 'html.parser')

for link in soup.find_all('h1'):
    link.string = 'new'
    print(link.get_text())

with open("templates/index.html", "w") as outf:
    outf.write(str(soup))
