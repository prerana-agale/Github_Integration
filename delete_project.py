# To delete the project

import requests
from pprint import pprint
from secret import TOKEN_VALUE

API_URL = 'https://api.github.com'
GITHUB_TOKEN = TOKEN_VALUE
HEADERS = {
    'Authorization': 'token ' + GITHUB_TOKEN,
    'Accept': 'application/vnd.github.inertia-preview+json'
}


def delete_project():
    delete_git_project = requests.delete(API_URL + '/projects/5783628',
                                         headers=HEADERS)
    pprint(delete_git_project.text)
