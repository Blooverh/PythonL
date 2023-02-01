cities=[] # create empty list

prompt="Enter 4 cities that you would like to visit: "
active=True
while active:
    city= input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

for i in range(5):
    city=input("Enter a city name up to 5 cities, if less just type quit to end program: ")
    if city== 'quit':
        break
    else:
        cities.append(city)

print(cities)