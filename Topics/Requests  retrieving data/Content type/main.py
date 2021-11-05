import requests


def get_content_type(url):
    resp = requests.get(url)
    return resp.headers['Content-Type']
