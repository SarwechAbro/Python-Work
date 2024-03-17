from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import string

url ='https://en.wikipedia.org/wiki/Main_Page'
source = requests.get(url)
soup = BeautifulSoup(source.text,'html.parser')

thm = soup.find('div', class_='thumbinner mp-thumb')

print(thm.text)