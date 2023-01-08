cars=["Audi", "bmw",'subaru','toyota']
for car in cars:
    if car== "Audi":
        print(car.upper())
    else:
        print(car.title())

car="Audi"
print(car=="audi") #false because Audi != to audi due to case

print(car.lower()=="audi") #ignoring the case by assigning lower case to variable

requestTopping= "cheese"
if requestTopping != "chorizo":
    print("dont use the chorizo")

addition=5+3
if addition > 5:
    print("5+3 > 5 is correct")

#CHECKING MULTIPLE CONDITIONS
result= (3*5)**2
if result >0 and result <10000:
    print("true")
print(result > 10000)
print(result < 1000)

toppings= ["cheese", "beef", "mushrooms"]
if "pepperoni" in toppings:
    print("pepperoni is in toppings hence true")
else:
    print("pepperoni not in toppings, hence false")

bestTopping="beef"
if bestTopping not in toppings:
    print(f"{bestTopping.title()}, is not in toppings ")
else:
    print(f"{bestTopping.title()}, is in toppings")

#boolean expressions
game_active=True
can_edit=False
print(game_active == can_edit)

can_edit=True
print(game_active == can_edit)

age= 15
if age < 10:
    print("entrance is $25")
elif age >= 15:
    print("The entrance is $50")
else:
    print("ENtrance is $35")

#5-3
alien_color=["red", "green", "yellow"]
if "red" in alien_color:
    print("you just won 5 points.")
if "blue" in alien_color:
    print("you wont 50 points")
else:
    print(False)

#5-4
alien_color=("green", "red", "yellow")
color= "red"

if color == alien_color[0]:
    print("you just earned 5 points")
elif color == alien_color[2]:
    print("you just earned 10 points")
elif color == alien_color[1]:
    print("you win 25 points")
else:
    print("you did not win anything")
print()
for i in alien_color:
    if i == "red":
        print("game over")
    elif i == "yellow":
        print("glitch in the game")
    elif i == "green":
        print("you won 50 points")

#5-8
users=["admin", "worker1", "worker2","worker3", "worker4"]
#users=[]
if len(users) ==0:
    print("we need more users")
for i in users:
    if i == "admin":
        print("hello admin!")
    else:
        print(f"{i.title()}, welcome! ")


#5-10
currUsers=["bloo","espadinsky", "Mungabula","RORO"]
newUsers=["roro", "biatch","Momma"]
newCurr= [i.lower() for i in currUsers]
for i in newUsers:
    if i.lower() in newCurr:
        print(f"{i} is being used, enter a new username")
    else:
        print(f"{i} username is available")



#5-11
list=[1,2,3,4,5,6,7,8,9]

for num in list:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num==3:
        print(f"{num}rd")
    else:
        print(f"{num}th")
