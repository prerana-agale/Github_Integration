# To get list of projects

import requests
from pprint import pprint
from secret import TOKEN_VALUE

API_URL = 'https://api.github.com'
GITHUB_TOKEN = TOKEN_VALUE
HEADERS = {
    'Authorization': 'token ' + GITHUB_TOKEN,
    'Accept': 'application/vnd.github.inertia-preview+json'
}


def get_projects():
    get_projects_list = requests.get(API_URL + '/users/prerana-agale/projects',
                                     headers=HEADERS)
    pprint(get_projects_list.json())
