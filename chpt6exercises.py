#6-7
personal_info_Diogo={
    "first_name":"Diogo",
    "last_name":"Aires",
    "age":23,
    "city":"Houston"
}

personal_info_Rohana={
    "first_name":"rohana",
    "last_name": "Kuriakose",
    "age":"20",
    "city":"dallas"
}

people={"person 1":personal_info_Diogo, "person 2":personal_info_Rohana}
#We access the value in the main dictionary with a loop
#each print we use the value of the main dictionary 
#by calling the value of the inside dictionaries 
#using the key of the inside dictionaries
for person, personInfo in people.items():
    full_name= f"{personInfo['first_name']} {personInfo['last_name']}"
    print(f"\nName of person is: {full_name.title()}")
    print(f"Age is: {personInfo['age']}")
    print(f"The city of this person is: {personInfo['city']}")

#6-8 Pets
dog={"type":"dog","breed":"shi tzu", "weight":20}
cat={"type":"cat","breed":"siamese", "weight":10}
snake={"type":"snake","breed":"python", "weight":5}

pets=[dog,snake,cat]

for info in pets:
    print(f"\nthe pet is a {info['type']} and its information is: ")
    print(f"Breed: {info['breed'].title()}")
    print(f"Weight: {info['weight']}")

print()
#6-9 Favorite places 
favorite_places={
    "Diogo": ["Lisbon","Dubai","Buenos Aires"],
    "Rohana":["Abu Dhabi","Houston"],
    "Lara":["Porto","Coimbra"]
}

for name, cities in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for city in cities:
        print(f"{city}") 

#6-11 Cities
cities={
    "Lisbon":{
        "country":"Portugal",
        "Museum":"Car museum"
    },
    "Dubai":{
        "country":"UAE",
        "Museum":"Dubai Museum"
    },
    "Houston":{
        "country":"USA",
        "Museum":"Fine arts museum"
    }
}

for city, info in cities.items():
    print(f"\nThe city is {city.title()} and 2 fun facts are:")
    print(f"Country: {info['country'].title()}")
    print(f"Museum: {info['Museum'].title()}")


