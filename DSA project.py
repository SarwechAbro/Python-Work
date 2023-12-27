from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

urls = []
Class = ''
title = ''
data = []

with open('links.txt', 'r') as links_file:
     links = links_file.readlines()
     for link in links:
          urls.append(link.strip())    
for url in urls:
     source = requests.get(url)
     soup = BeautifulSoup(source.text,'html.parser')
     headers = soup.find_all('div', class_='post-header-title')
     contents = soup.find_all('div', class_='entry-content clearfix single-post-content')
     print(url)
     for header in headers: 
          badges = header.find_all('div', class_='term-badges floated')
          for badge in badges:
               spans = badge.find_all('span')
               for span in spans: 
                    Class = span.get('class')
                    class_name = ' '.join(Class)   
                    if class_name != 'term-badge term-40':
                         title = span.a.text
                         print(title) 
                         break 
     for content in contents:
          paragraph = content.find('p')
          if paragraph:
               text = paragraph.text.strip('.')
               text = text.replace("\n", "")
               newss = re.split(r'\.(?!\d)', text)
               if '' in newss: 
                    newss.remove('')
               for news in newss:
                    data.append([title,news])

df = pd.DataFrame(data, columns=["Titles", "News"])
df.to_csv("news.csv", index=False)
print(len(data))


