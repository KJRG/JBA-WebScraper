from bs4 import BeautifulSoup
from string import punctuation

import os
import os.path
import requests


ARTICLE_LIST_URL = "https://www.nature.com/nature/articles?sort=PubDate&year=2020"
STATUS_CODE_OK = 200


def download_articles(num_pages, article_type):
    for i in range(1, num_pages + 1):
        download_articles_from_page(i, article_type)


def download_articles_from_page(page_num, article_type):
    page_dir_name = os.path.join(os.getcwd(), f"Page_{page_num}")
    os.mkdir(page_dir_name)
    resp = requests.get(ARTICLE_LIST_URL, params={"sort": "PubDate", "year": 2020, "page": page_num})
    if resp.status_code != STATUS_CODE_OK:
        return
    soup = BeautifulSoup(resp.content, "html.parser")
    articles = soup.find_all("article")
    for article in articles:
        if extract_article_type(article) == article_type:
            download_article(get_article_url(article), page_dir_name)


def extract_article_type(article_tag):
    return article_tag.find("span", {"class": "c-meta__type"}).text


def get_article_url(article_tag):
    article_link_a_tag = article_tag.find("a", {"data-track-action": "view article"})
    partial_article_url = article_link_a_tag.get("href")
    return f"https://www.nature.com{partial_article_url}"


def download_article(article_url, dir_name):
    resp = requests.get(article_url)
    if resp.status_code != STATUS_CODE_OK:
        return ""
    soup = BeautifulSoup(resp.content, "html.parser")
    article_title = extract_article_title(soup)
    article_file_name = f"{sanitize_file_name(article_title)}.txt"
    article_text = extract_article_text(soup)
    save_article(bytes(article_text, "utf-8"), os.path.join(dir_name, article_file_name))


def extract_article_title(soup):
    return soup.find("h1").text


def extract_article_text(soup):
    return soup.find("div", {"class": "c-article-body u-clearfix"}).text


def sanitize_file_name(txt):
    txt = txt.rstrip()
    txt = txt.translate(str.maketrans(" ", "_", punctuation))
    return txt


def save_article(page_content, file_name):
    with open(file_name, "wb") as page_file:
        page_file.write(page_content)


def main():
    num_pages = int(input())
    article_type = input()
    download_articles(num_pages, article_type)
    print("Saved all articles.")


if __name__ == "__main__":
    main()
