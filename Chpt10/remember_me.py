import json 

fileName="username.json"

def greet_user():
    try:
        with open(fileName) as f:
            username=json.load(f)
    except FileNotFoundError:
        username = input("what is your user name ?")
        with open(fileName,'w') as f:
            json.dump(username,f)
            print(f"We will remeber you when you comeback {username} !")
    else:
        print(f"Welcome back {username} !")

greet_user()

