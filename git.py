from github import Github

# or using an access token
g = Github("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")
repo = g.get_repo("2BlackCats/test_repo")

## Complete your tasks from here

print(repo)