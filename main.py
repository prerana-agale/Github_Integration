from github import Github


class Git_hub:
    global g, username, password
    username = input('Enter username:')
    # password=input('Enter password:')

    g = Github('c5441454e7f9e7e6039fb14fc3869e27975e6e7c')

    def get_repos(self):
        repos = g.get_user().get_repos()
        for repo in repos:
            print(repo.name)

    def get_user(self):
        user = g.get_user()
        print(user.login)

    def get_user_byname(self):
        user = g.get_user(username)
        print(user.name)

    def get_repo_byname(self):
        repository = input("enter repo name")
        repo = g.get_repo("prerana-agale/LP3")
        print(repo.name)
        print(repo.get_views_traffic())

    def get_content(self):
        repo = g.get_repo("prerana-agale/LP3")
        contents = repo.get_contents("rsa")  # specific file
        for content in contents:
            print(content)

    def create_new_repo(self):
        try:
            user = g.get_user()
            repo = user.create_repo("Test")
        except:
            print("Repository already exists")
        else:
            print("Repository created successfully")

    def add_file_torepo(self):
        try:
            repo = g.get_repo("prerana-agale/Test")
            repo.create_file("test.txt", "test", "test", branch="test")
        except:
            print("Cannot add file")
        else:
            print("File added!!")

    def update_file(self):
        try:
            repo = g.get_repo("prerana-agale/Test")
            contents = repo.get_contents("test.txt", ref="test")
            repo.update_file(contents.path, "this is text", "this is text", contents.sha, branch="test")
        except:
            print("cannot update")
        else:
            print("Updated")

    def delete_file(self):
        try:
            repo = g.get_repo("prerana-agale/Test")
            contents = repo.get_contents("test.txt", ref="test")
            repo.delete_file(contents.path, "remove test", contents.sha, branch="test")
        except:
            print("cannot delete")
        else:
            print("Deleted")

    def delete_repo(self):
        try:
            repo = g.get_repo("prerana-agale/Test")
            repo.delete()
        except:
            print("cannot delete")
        else:
            print("Deleted")


p = Git_hub()

while True:
    print(
        "\n1.Get user details\n2.Get repos\n3.create Repo\n4.Add file\n5.update file\n6.Get repo by name"
        "\n7.Delete file in Repo\n8.Get content\n9.Delete Repo\n")
    num = int(input("\n\nEnter your choice (or 0 to quit):"))
    if num == 0:
        break

    elif num == 1:
        p.get_user()
        p.get_user_byname()

    elif num == 2:
        p.get_repos()

    elif num == 3:
        p.create_new_repo()

    elif num == 4:
        p.add_file_torepo()

    elif num == 5:
        p.update_file()

    elif num == 6:
        p.get_repo_byname()

    elif num == 7:
        p.delete_file()

    elif num == 8:
        p.get_content()

    elif num == 9:
        p.delete_repo()

    else:
        print("enter correct option:")
