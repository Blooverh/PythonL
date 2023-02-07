def get_formatted_name(first_name, last_name):
    full_name= f"{first_name} {last_name}"
    return full_name.title()

soccer_player= get_formatted_name("diogo", "aires")
print(soccer_player)

#RETURNING A DICTIONARY

def build_person(first_name, last_name):
    person= {'first':first_name, 'last':last_name}
    return person

person= build_person("Diogo", "Aires")
print(person)