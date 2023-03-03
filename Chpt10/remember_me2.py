import json 

def get_stored_username():
    """Get stored username if available"""
    fileName= 'usernames.json'
    try:
        with open(fileName) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else: 
        return username
    
def get_new_username():
    """Prompt for new user name"""
    username= input("What is your username? ")
    fileName='usernames.json'
    with open(fileName,'w') as f:
        json.dump(username,f)
    return username
    
def greet_user():
    """Greet the user by username"""
    username= get_stored_username()
    if username:
        print(f"Welcome back {username}!")
    else:
        username= get_new_username()
        print(f"We will remember you {username} !")

greet_user()
