from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import pandas as pd
import numpy as np
import re
import string


data = []
title = ''
urls = ['https://awamiawaz.pk/category/latest-news','https://awamiawaz.pk/category/sindh-news',
'https://awamiawaz.pk/category/awami-awaz-tv','https://awamiawaz.pk/category/national',
'https://awamiawaz.pk/category/todays-newspaper','https://awamiawaz.pk/category/articles',
'https://awamiawaz.pk/category/international','https://awamiawaz.pk/category/sports',
'https://awamiawaz.pk/category/entertainment','https://awamiawaz.pk/category/health',
'https://awamiawaz.pk/category/special-reports','https://awamiawaz.pk/category/science-technology',
'https://awamiawaz.pk/category/interesting-weird']
for url in urls:
     source = requests.get(url)
     soup = BeautifulSoup(source.text,'html.parser')
     contents = soup.find_all('div', class_='bs-pagination-wrapper main-term-none more_btn')
     sections = soup.find_all('section', class_='archive-title category-title with-actions with-terms')

     for section in sections: 
          title = section.h1.span.text
     for content in contents:             
          girds = content.find_all('div', class_='listing listing-grid listing-grid-1 clearfix columns-3')
          for gird in girds:
               articles = gird.find_all('article')
               for article in articles:
                    items = article.find_all('div', class_='item-inner')
                    for item in items:
                         post_summary = item.find('div', class_='post-summary')
                         data.append([title,post_summary.text.strip()])

df = pd.DataFrame(data, columns=["Titles", "Headings"])
df.to_csv("news.csv", index=False)
print(len(data))


