# To delete the repository

import requests
from pprint import pprint
from secret import TOKEN_VALUE

API_URL = 'https://api.github.com'
GITHUB_TOKEN = TOKEN_VALUE
HEADERS = {
    'Authorization': 'token ' + GITHUB_TOKEN,
    'Accept': 'application/vnd.github.inertia-preview+json'
}


def delete_repo():
    delete_git_repo = requests.delete(API_URL + '/repos/prerana-agale/test',
                                      headers=HEADERS)
    pprint(delete_git_repo.text)
