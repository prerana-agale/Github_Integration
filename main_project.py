from user_details import user_details
from get_repositories import get_repos
from create_repository import create_repo
from update_repository import update_repo
from delete_repository import delete_repo
from create_project import create_project
from get_projects import get_projects
from update_project import update_project
from delete_project import delete_project

while True:
    print(
        '\n1.Get user details\n2.Get repos\n3.create Repo\n4.Update Rpo\n'
        '5.Delete Repo\n6.Get projects\n7.Create project\n8.Update project\n'
        '9.Delete project')
    num = int(input('\nEnter your choice (or 0 to quit):'))
    if num == 0:
        break

    elif num == 1:
        user_details()

    elif num == 2:
        get_repos()

    elif num == 3:
        create_repo()

    elif num == 4:
        update_repo()

    elif num == 5:
        delete_repo()

    elif num == 6:
        get_projects()

    elif num == 7:
        create_project()

    elif num == 8:
        update_project()

    elif num == 9:
        delete_project()

    else:
        print('enter correct option:')
