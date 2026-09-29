#I made a list of users, then a list of new users, then a list of those names in lowercase form, finally checking each new username to see if it is already being used.

current_users = ["zach", "eric", "ryan", "nick", "cole"]

new_users = ["james", "connor", "collin", "mike", "john"]

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(user + " will need to enter a new username.")
    else:
        print(user + " is available.")
