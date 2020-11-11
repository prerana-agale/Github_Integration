# To create new repository

import requests
from pprint import pprint
from secret import TOKEN_VALUE


API_URL = 'https://api.github.com'
GITHUB_TOKEN = TOKEN_VALUE
HEADERS = {
    'Authorization': 'token ' + GITHUB_TOKEN,
    'Accept': 'application/vnd.github.inertia-preview+json'
}


def create_repo():
    create_new_repo = requests.post(API_URL + '/user/repos',
                                    data='{"name":"test"}',
                                    headers=HEADERS)
    pprint(create_new_repo.json())
