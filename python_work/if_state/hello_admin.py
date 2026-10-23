# create a list of usernames

usernames = []
#usernames = ['admin', 'Samuel', 'Michael', 'Julius', 'Kimberly']

# check for empty list
if usernames:
    for user in usernames:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")
