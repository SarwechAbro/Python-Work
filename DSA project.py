from bs4 import BeautifulSoup
import lxml
import requests
import pandas as pd
import numpy as np



url = 'https://books.sindhsalamat.com/book/87/read/2843'
source = requests.get(url)
soup = BeautifulSoup(source.text,'html.parser')

for paragraph in soup.find_all('article', class_='row card article-row'):
     article = paragraph.main.p.text
     

url = 'https://books.sindhsalamat.com/book/87/read/2838'
source = requests.get(url)
soup = BeautifulSoup(source.text,'html.parser')

for paragraph in soup.find_all('article', class_='row card article-row'):
     article2 = paragraph.main.p.text
     
     merged_articles = article + " " + article2
     My_list = merged_articles.split()
     #encoded_string = merged_articles.encode('utf-16')
    # with open('python.txt', 'wb') as f:
     # f.write(encoded_string)
      #f.close()
     print(My_list)
    
     