from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'https://jang.com.pk/news/1303412'
source = requests.get(url)
soup = BeautifulSoup(source.text, 'lxml')
newss = []
data = []
paras = soup.find_all('div', class_='detail_view_content')
for para in paras:
    ps = para.find_all('p')
    for d in ps:
        p = d.text
        newss = p.split('.')
        for news in newss:
            print(news)
            data.append(['pakistan',news])


df = pd.DataFrame(data, columns=["Titles", "Headings"])
df.to_csv("abrar.csv", index=False)
print(len(data))