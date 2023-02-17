def greet_user(names): #passes a list called names
    for name in names:
        msg=f"Hello {name.title()}!"
        print(msg)

usernames=['Diogo', 'Rohana', 'Lara']
greet_user(usernames)

