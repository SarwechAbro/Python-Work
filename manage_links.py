links = set()
with open('working_urls.txt', 'r') as working_urls:
    for url in working_urls:
        links.add(url)

with open('final_urls.txt', 'w') as file:
    for link in links:
        file.write(f'{link}')  
print(len(links))