from bs4 import BeautifulSoup
import lxml
import requests
import pandas as pd
import numpy as np
import re
import string



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
     my_list = list(set(merged_articles.split())) 
     #encoded_string = my_set.encode('utf-16')
     #with open('python.txt', 'w') as f:
          #f.write(my_set)
          #f.close()


 

my_list = [''.join(c for c in s if c not in string.punctuation + "؛؟،’’– ََ؛") for s in my_list]
my_list = [word for word in my_list if not re.search(r'[a-zA-Z]', word)]
encoded_list = ' '.join(my_list).encode('utf-8')
with open('Book.txt', 'wb') as f:
      f.write(encoded_list)
      f.close()

#for word in my_list:
      #print(word)
