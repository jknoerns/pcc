current_users = ['JOHN', 'MICHELLE', 'David', 'Billy', 'Kathy']
cp_current_users = []
for user in current_users:
    cp_current_users.append(user.lower())

new_users = ['alyssa', 'alden', 'john', 'billy', 'linda']
for user in new_users:
    if user.lower() in cp_current_users:
        print(f"Username {user} is not avaiable. Please choose another.")
    else:
        print(f"Username {user} is available.")
