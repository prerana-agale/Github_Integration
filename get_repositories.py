# To get list of repositories

import requests
from pprint import pprint
from secret import TOKEN_VALUE

API_URL = 'https://api.github.com'
GITHUB_TOKEN = TOKEN_VALUE
HEADERS = {
    'Authorization': 'token ' + GITHUB_TOKEN,
    'Accept': 'application/vnd.github.inertia-preview+json'
}


def get_repos():
    get_repos_list = requests.get(API_URL + "/user/repos", headers=HEADERS)
    pprint(get_repos_list.json())
