import requests

def http_post(url):
    result = requests.post(url)
    return result