import requests
from bs4 import BeautifulSoup
import time

query = "google"
url = "https://www.bing.com/search?q=" + query
headers = {"User-Agent": "Mozilla/5.0"} # to avoid being blocked by Bing
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
results = soup.find_all("li", class_="b_algo") # get the list of results
for result in results: # loop through the first 10 results
    title = result.find("h2").text # get the title
    snippet = result.find("p").text # get the snippet
    link = result.find("a")["href"] # get the link
    value=(title, snippet, link) # print the information
    for char in value:
       print(char , end=' ', flush=True)
       time.sleep(0.6) 