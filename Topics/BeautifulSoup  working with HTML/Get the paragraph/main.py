import requests

from bs4 import BeautifulSoup


word_to_find = input()
url = input()

resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html.parser')
all_paragraphs = soup.find_all('p')
for p in all_paragraphs:
    if word_to_find in p.text:
        print(p.text)
        break
