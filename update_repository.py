# Update Repository

import requests
from pprint import pprint
from secret import TOKEN_VALUE

API_URL = 'https://api.github.com'
GITHUB_TOKEN = TOKEN_VALUE
HEADERS = {
    'Authorization': 'token ' + GITHUB_TOKEN,
    'Accept': 'application/vnd.github.inertia-preview+json'
}


def update_repo():
    update_user_repo = requests.patch(API_URL + '/repos/prerana-agale/test',
                                      data='{"name":"test1"}',
                                      headers=HEADERS)
    pprint(update_user_repo.json())
