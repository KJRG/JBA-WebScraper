import requests

from bs4 import BeautifulSoup


act_number = int(input())
url = input()

resp = requests.get(url)

soup = BeautifulSoup(resp.content, 'html.parser')

a_tag_list = soup.find_all('a')
act_link_index = act_number - 1
act_link = a_tag_list[act_link_index].get('href')
print(act_link)
