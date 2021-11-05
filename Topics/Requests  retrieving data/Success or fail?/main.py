import requests


def check_success(url):
    resp = requests.get(url)
    return "Success" if resp else "Fail"
