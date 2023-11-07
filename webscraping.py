from bs4 import BeautifulSoup
import lxml
import requests
import pandas as pd
import numpy as np

url = 'https://pahenjiakhbar.com/'
source = requests.get(url).text
soup = BeautifulSoup(source,'lxml')
for text in soup.find_all('div', class_='fusion-column-wrapper fusion-column-has-shadow fusion-flex-justify-content-flex-start fusion-content-layout-column'):
     news = text.ul.li.text
     print(news)
