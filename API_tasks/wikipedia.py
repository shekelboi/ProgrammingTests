import requests

BASE_URL = 'https://en.wikipedia.org/w/api.php'

default_items = {
    'action': 'parse',
    'format': 'json'
}

params = {
    **default_items,
    'page': 'Nicoll Highway collapse',
    'prop': 'categories',
}

response = requests.get(BASE_URL, params=params)
categories = response.json()['parse']['categories']
print([c['*'] for c in categories if 'hidden' not in c])
