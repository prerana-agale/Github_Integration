import requests
from pprint import pprint
from secret import Token_Value

API_URL = "https://api.github.com"
GITHUB_TOKEN = Token_Value
headers = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.inertia-preview+json"
}

user_details = requests.get(API_URL + "/user", headers=headers)
get_repos = requests.get(API_URL + "/user/repos", headers=headers)
create_repo = requests.post(API_URL + "/user/repos", data='{"name":"PreranaAgale"}', headers=headers)
get_projects = requests.get(API_URL + "/users/preranaagale/projects", headers=headers)
#delete_repo = requests.delete(API_URL + "/repos/preranaagale/PreranaAgale123", headers=headers)
update_repo = requests.patch(API_URL + "/repos/prerana-agale/Testing_1", data='{"name":"New Demo"}', headers=headers)
create_project = requests.post(API_URL + "/user/projects", data='{"name":"Prerana"}', headers=headers)
update_project = requests.patch(API_URL + "/projects/5768902", data='{"name":"Testing"}', headers=headers)
proj_in_repo = requests.post(API_URL+"/repos/prerana-agale/Testing/projects", data='{"name":"New Demo"}', headers=headers)

print(
    "\n1.Get user details\n2.Get repos\n3.create Repo\n4.Update Rpo\n5.Delete Repo\n6.Get projects\n7.Create "
    "project\n8.Update project\n9. Create Project In Repo")

while True:
    num = int(input("\n\nEnter your choice (or 0 to quit):"))
    if num == 0:
        break

    elif num == 1:
        pprint(user_details.json())

    elif num == 2:
        pprint(get_repos.json())

    elif num == 3:
        pprint(create_repo.json())

    elif num == 4:
        pprint(update_repo.json())

    elif num == 5:
        try:
            response = requests.delete(API_URL + "/repos/preranaagale/New-Demo12344", headers=headers)
        except:
            print("Cannot delete repo!!")
        else:
            print(response.text)

    elif num == 6:
        pprint(get_projects.json())

    elif num == 7:
        pprint(create_project.json())

    elif num == 8:
        pprint(update_project.json())

    elif num == 9:
        pprint(proj_in_repo.json())

    else:
        print("enter correct option:")

