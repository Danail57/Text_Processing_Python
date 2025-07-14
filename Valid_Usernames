usernames = input().split(", ")
not_allowed = [""]

for user in usernames:
    if len(user) not in range(3, 16 + 1):
        continue
    if any(character in not_allowed for character in usernames):
        continue
    if all(character.isalnum() or character in ("-", "_") for character in user):
        print(user)
