import requests

from bs4 import BeautifulSoup


url = input()
resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html.parser')
print(soup.find('h1').text)
