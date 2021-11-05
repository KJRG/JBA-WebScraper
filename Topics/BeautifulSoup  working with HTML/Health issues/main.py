import requests

from bs4 import BeautifulSoup


TOPIC_START_LETTER = 'S'


def is_matching_topic(a_tag):
    text = a_tag.text
    href = a_tag.get('href')
    return len(text) > 1 and text.startswith(TOPIC_START_LETTER) and ('entity' in href or 'topics' in href)


url = input()

resp = requests.get(url)

soup = BeautifulSoup(resp.content, 'html.parser')

topics = [a.text for a in soup.find_all('a') if is_matching_topic(a)]
print(topics)
