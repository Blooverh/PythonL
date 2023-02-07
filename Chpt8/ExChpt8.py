# Normal function with no default value
# def make_shirt(size, message):
#     print(f"The size chosen for the t-shirt was {size.title()}")
#     print(f"and the message you want printed is: {message.title()}")

# message= input("What message do you wish to put in the shirt? ")
# make_shirt('L',message)

#with defaul value
def make_shirt(message, size='L'):
    print(f"The size chosen for the t-shirt was {size}")
    print(f"and the message you want printed is: {message.title()}")

message= input("What message do you wish to put in the shirt? ")
make_shirt(message)

def describe_city(city, country):
    print(f"your favorite city is {city.title()}, and it belongs to the following country: {country.title()}")


prompt= input("What is your favorite city? ")
prompt2= input("WHich country is that city located? ")

describe_city(prompt, prompt2)

def city_country(city, country):
    print(f'"{city.title()}, {country.title()}"')

city_country("Lisbon", "portugal")
city_country("santiago", "chile")
