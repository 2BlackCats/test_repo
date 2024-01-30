from github import Github

# or using an access token
g = Github("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")
repo = g.get_repo("2BlackCats/test_repo")

## Complete your tasks from here

print(list(repo.get_branches()))

pulls = repo.get_pulls()

for pr in pulls:
    print(pr.number)

commit = repo.get_commits()
for cm in commit:
    print(cm)