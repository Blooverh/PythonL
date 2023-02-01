active =True
toppings=[]
while active:
    topping= input("Enter several pizza toppings, when done write quit: ")
    if topping=='quit':
        active=False
    else:
        toppings.append(topping)
print()
for i in range(len(toppings)):
    print(f"You entered the following toppings:{toppings[i].title()} ")

