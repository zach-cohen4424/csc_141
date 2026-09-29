#This program contains some useful commands using lists, for loops, and if statemnets. 
#Difficult level 8/10
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, how are you?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")
