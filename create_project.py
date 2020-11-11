# To create new project

import requests
from pprint import pprint
from secret import TOKEN_VALUE

API_URL = 'https://api.github.com'
GITHUB_TOKEN = TOKEN_VALUE
HEADERS = {
    'Authorization': 'token ' + GITHUB_TOKEN,
    'Accept': 'application/vnd.github.inertia-preview+json'
}


def create_project():
    create_new_project = requests.post(API_URL + '/user/projects',
                                       data='{"name":"Prerana"}',
                                       headers=HEADERS)
    pprint(create_new_project.json())
