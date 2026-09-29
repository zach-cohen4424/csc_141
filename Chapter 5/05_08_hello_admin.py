#This program contrain some useful commans using lists, for loops, and if statements. 
usernames = ['admin', 'zach', 'eric', 'ryan', 'nick']     

for username in usernames:
    if username == 'admin':
        print("Hello admin, how are you?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")
