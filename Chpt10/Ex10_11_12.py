import json

""" Gets the favorite number to the user and writes it in json file 
Also returns the name from function call"""
def get_fav_num():
    fav_num= input("What is your favorite number? ")
    fileName='fav_num.json'
    with open(fileName, 'w') as f:
        json.dump(fav_num, f)
    return fav_num

""" gets from the json file the number, if the file exists
if it does return the data from function call that was acquired from the json file"""
def get_stored_num():
    fileName='fav_num.json'
    try:
        with open(fileName) as f:
            fav_num=json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_num
""" Gets the fav number from method that reads the number from json file 
if it exists tells user what number it is to confirm
If it does not exists, new data is created and tells user it will be remembered"""
def tell_fav_num():
    """Tell user its favorite  number and that we will remember it"""
    fav_num=get_stored_num()
    if fav_num:
        print(f"Your favorite number is {fav_num} correct? ")
    else:
        fav_num= get_fav_num()
        print(f"We will remember that your favorite number is {fav_num} !")

tell_fav_num()