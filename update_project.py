# Update the project

import requests
from pprint import pprint
from secret import TOKEN_VALUE

API_URL = 'https://api.github.com'
GITHUB_TOKEN = TOKEN_VALUE
HEADERS = {
    'Authorization': 'token ' + GITHUB_TOKEN,
    'Accept': 'application/vnd.github.inertia-preview+json'
}


def update_project():
    update_user_project = requests.patch(API_URL + '/projects/5783628',
                                         data='{"name":"Prerana A"}',
                                         headers=HEADERS)
    pprint(update_user_project.json())
