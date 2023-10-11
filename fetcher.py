import requests


def fetch(category, word):
    API_KEY = '<FILL IN>'
    url = 'https://pixabay.com/api/'
    params = {
        "key": API_KEY,
        "q": f'{word}+{category}',
    }
    imageLinks = []
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        results = data.get("hits", [])
        for res in results[:10]:
            imageLinks.append(res['webformatURL'])
    return imageLinks
