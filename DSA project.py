from bs4 import BeautifulSoup
import lxml
import requests
import pandas as pd
import numpy as np

url = 'https://books.sindhsalamat.com/book/87/read/2838'
source = requests.get(url)
soup = BeautifulSoup(source.text,'html.parser')

for paragraph in soup.find_all('article', class_='row card article-row'):
     article = paragraph.main.p.text
     mylist = article.split()
     print(mylist)