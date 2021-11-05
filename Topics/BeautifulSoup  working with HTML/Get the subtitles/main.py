import requests

from bs4 import BeautifulSoup


subtitle_index = int(input())
url = input()

resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html.parser')
all_subtitle_tags = soup.find_all('h2')
print(all_subtitle_tags[subtitle_index].text)
