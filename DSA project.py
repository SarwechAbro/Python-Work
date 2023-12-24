from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import pandas as pd
import numpy as np
import re
import string

class_name = ''
data = []
title = []
urls = [
     'https://awamiawaz.pk/1147426','https://awamiawaz.pk/1147382','https://awamiawaz.pk/1147685',
     'https://awamiawaz.pk/1147647','https://awamiawaz.pk/1147383','https://awamiawaz.pk/1147389'
     'https://awamiawaz.pk/1147638','https://awamiawaz.pk/1147632','https://awamiawaz.pk/1147620',
     'https://awamiawaz.pk/1147611','https://awamiawaz.pk/1147594','https://awamiawaz.pk/1147584',
     'https://awamiawaz.pk/1147581','https://awamiawaz.pk/1147562','https://awamiawaz.pk/1147590',
     'https://awamiawaz.pk/1147491','https://awamiawaz.pk/1147375','https://awamiawaz.pk/1147373',
     'https://awamiawaz.pk/1147359','https://awamiawaz.pk/1147356','https://awamiawaz.pk/1147328',
     'https://awamiawaz.pk/1147311','https://awamiawaz.pk/1147239','https://awamiawaz.pk/1147215',
     'https://awamiawaz.pk/1147135','https://awamiawaz.pk/1147110','https://awamiawaz.pk/1147085',
     'https://awamiawaz.pk/1147076','https://awamiawaz.pk/1147022','https://awamiawaz.pk/1147015',
     'https://awamiawaz.pk/1147010','https://awamiawaz.pk/1147703','https://awamiawaz.pk/1147702',
     'https://awamiawaz.pk/1147806','https://awamiawaz.pk/1147528','https://awamiawaz.pk/1147529',
     'https://awamiawaz.pk/1147526','https://awamiawaz.pk/1147527','https://awamiawaz.pk/1147538',
     'https://awamiawaz.pk/1147170','https://awamiawaz.pk/1147173','https://awamiawaz.pk/1147174',
     'https://awamiawaz.pk/1147175','https://awamiawaz.pk/1147578','https://awamiawaz.pk/1147096',
     'https://awamiawaz.pk/1146977','https://awamiawaz.pk/1146973','https://awamiawaz.pk/1146634',
     'https://awamiawaz.pk/1146623','https://awamiawaz.pk/1146541','https://awamiawaz.pk/1146520',
     'https://awamiawaz.pk/1146180','https://awamiawaz.pk/1146149','https://awamiawaz.pk/1146100',
     'https://awamiawaz.pk/1146086','https://awamiawaz.pk/1145756','https://awamiawaz.pk/1145729',
     'https://awamiawaz.pk/1145683','https://awamiawaz.pk/1145679','https://awamiawaz.pk/1145445',
     'https://awamiawaz.pk/1145435','https://awamiawaz.pk/1145354','https://awamiawaz.pk/1147617',
     'https://awamiawaz.pk/1147603','https://awamiawaz.pk/1147563','https://awamiawaz.pk/1147506',
     'https://awamiawaz.pk/1147378','https://awamiawaz.pk/1147367','https://awamiawaz.pk/1147031',
     'https://awamiawaz.pk/1147026','https://awamiawaz.pk/1147012','https://awamiawaz.pk/1146677',
     'https://awamiawaz.pk/1146654','https://awamiawaz.pk/1146517','https://awamiawaz.pk/1146323',
     'https://awamiawaz.pk/1146309','https://awamiawaz.pk/1146190','https://awamiawaz.pk/1146133',
     'https://awamiawaz.pk/1145860','https://awamiawaz.pk/1145857','https://awamiawaz.pk/1145853'
     ]
for url in urls:
     source = requests.get(url)
     soup = BeautifulSoup(source.text,'html.parser')
     headers = soup.find_all('div', class_='post-header-title')
     contents = soup.find_all('div', class_='entry-content clearfix single-post-content')

     for header in headers: 
          badges = header.find_all('div', class_='term-badges floated')
          for badge in badges:
               spans = badge.find_all('span')
               for span in spans: 
                    class_name = span.get('class')
                    class_name_string = ' '.join(class_name)   
                    if class_name_string != 'term-badge term-40':
                         title = span.a.text
                         print(title) 
                    else:
                         continue                 
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

df = pd.DataFrame(data, columns=["Titles", "Headings"])
df.to_csv("news.csv", index=False)
print(len(data))


