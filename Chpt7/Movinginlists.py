unconfirmed_users=['Alice','Bryan','Candace']
confirmed_users=[]

while unconfirmed_users: #verifies each user until there is no more
    current_user=unconfirmed_users.pop() #everytime u pop unconfirmed user from list assign it to current user to store it in confirmed user list
    print(f"Veryfying user: {current_user.title()}")
    confirmed_users.append(current_user)
    print(f"Following users have been confirmed.")
    for user in confirmed_users:
        print(user.title())