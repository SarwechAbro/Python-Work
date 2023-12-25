import csv
from bs4 import BeautifulSoup
import requests

def extract_data_from_url(url):
    # Fetch the HTML content of the page
    source = requests.get(url).text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(source, 'lxml')

    # Extract the news headline
    url_for_headline = 'https://www.bbc.com/urdu/topics/cjgn7n9zzq7t'
    source_for_headline = requests.get(url_for_headline).text
    soup_for_headline = BeautifulSoup(source_for_headline, 'lxml')
    
    for heading in soup_for_headline.find_all('div', class_='bbc-wthhiv'):
        news_headline = heading.h1.text

    # Extract the news text along with links
    news_text = ''
    for text in soup.find_all('div', class_='bbc-4wucq3 ebmt73l0'):
        paragraphs = text.find_all('p')
        for paragraph in paragraphs:
            news_text += paragraph.text + '\n'

    return {'Text': news_text, 'Heading': news_headline}

# List of URLs
urls = [
    'https://www.bbc.com/urdu/articles/cjrpj2x277ro',    'https://www.bbc.com/urdu/articles/c8429rmxrvpo' ,'https://www.bbc.com/urdu/articles/cx71zg6597jo','https://www.bbc.com/urdu/articles/cd1p5x1242qo','https://www.bbc.com/urdu/articles/c4ny70pxeppo','https://www.bbc.com/urdu/articles/cnd73x23n0yo','https://www.bbc.com/urdu/articles/cyx2zgxppp0o','https://www.bbc.com/urdu/articles/cd1p0nnpz3do','https://www.bbc.com/urdu/articles/c3g2xdngpglo','https://www.bbc.com/urdu/articles/c3g23dyjjp0o','https://www.bbc.com/urdu/articles/cd1pqe52qjqo','https://www.bbc.com/urdu/articles/clwp7v3nxepo','https://www.bbc.com/urdu/articles/ck5p374py7ro','https://www.bbc.com/urdu/articles/cp9p81wd2ejo','https://www.bbc.com/urdu/articles/cnkp1dlydn7o','https://www.bbc.com/urdu/articles/c9739p4gqj6o','https://www.bbc.com/urdu/articles/c8089le3eddo','https://www.bbc.com/urdu/articles/ce7p4j8n8reo','https://www.bbc.com/urdu/articles/c102qgqglvro','https://www.bbc.com/urdu/articles/c3g272y4x9vo','https://www.bbc.com/urdu/articles/cw0283gl15po','https://www.bbc.com/urdu/articles/c3g2vj10j0yo','https://www.bbc.com/urdu/articles/c0x2q9q06j5o','https://www.bbc.com/urdu/articles/c72q46qv23zo','https://www.bbc.com/urdu/articles/c4n0zgg5r5yo','https://www.bbc.com/urdu/articles/cj7p2xpzv5po','https://www.bbc.com/urdu/articles/c4n9q7p0dl5o','https://www.bbc.com/urdu/articles/c51e27lmpg7o','https://www.bbc.com/urdu/articles/c0j28dwvvn5o','https://www.bbc.com/urdu/articles/crgpxl9dneno','https://www.bbc.com/urdu/articles/cnkp8wenvq2o','https://www.bbc.com/urdu/articles/cxr1e6ze09wo','https://www.bbc.com/urdu/articles/cqvpgwzpj1eo','https://www.bbc.com/urdu/articles/cp6p3p75elpo','https://www.bbc.com/urdu/articles/cyx2nl4jypwo'
   
]

def extract_data_from_khel(url1):
    # Fetch the HTML content of the page
    source = requests.get(url1).text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(source, 'lxml')

    # Extract the news headline
    url_for_headline = 'https://www.bbc.com/urdu/topics/c340q0p2585t'
    source_for_headline = requests.get(url_for_headline).text
    soup_for_headline = BeautifulSoup(source_for_headline, 'lxml')
    
    for heading in soup_for_headline.find_all('div', class_='bbc-wthhiv'):
        news_headline = heading.h1.text

    # Extract the news text along with links
    news_text = ''
    for text in soup.find_all('div', class_='bbc-4wucq3 ebmt73l0'):
        paragraphs = text.find_all('p')
        for paragraph in paragraphs:
            news_text += paragraph.text + '\n'
           

    return {'Text': news_text, 'Heading': news_headline}


urll = [
    'https://www.bbc.com/urdu/articles/c972e91v7ezo'
    ,'https://www.bbc.com/urdu/articles/cw8038e404lo'
    ,'https://www.bbc.com/urdu/articles/cmljm104mz7o'
    ,'https://www.bbc.com/urdu/articles/cgrpr53gzzeo'
    ,'https://www.bbc.com/urdu/articles/ckvp7k1kveeo'
    ,'https://www.bbc.com/urdu/articles/c0d24gm2yg3o'
    ,'https://www.bbc.com/urdu/articles/cz92g90g25zo'
    ,'https://www.bbc.com/urdu/articles/cy92kgqep5vo'
    ,'https://www.bbc.com/urdu/articles/cg3p87dnyngo'
    ,'https://www.bbc.com/urdu/articles/cl5pwge03y0o'
    ,'https://www.bbc.com/urdu/articles/cmlpngev2x7o'
    ,'https://www.bbc.com/urdu/articles/c72dpyznz4xo'
    ,'https://www.bbc.com/urdu/articles/cv2rjyywwd3o'
    ,'https://www.bbc.com/urdu/articles/cd1001d34e7o'
    ,'https://www.bbc.com/urdu/articles/cnkg078v294o'
    ,'https://www.bbc.com/urdu/articles/cd1zkgwwyyqo'
    
     ]

# Write data to CSV file
csv_filename = 'news_data.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Text', 'Heading']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data for each URL
    for url in urls:
        data = extract_data_from_url(url)
        writer.writerow(data)
   
    fieldnames = ['Text', 'Heading']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data for each URL
    for url1 in urll:
        data = extract_data_from_khel(url1)
        writer.writerow(data)
   
print(f'Data has been written to {csv_filename}')