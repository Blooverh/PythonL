# Working with lists

# 4-1
pizzaTypes = ["hawaian", "beef", "cheese"]
for i in pizzaTypes:
    print(f"I like {i.title()} pizza")
print(f"I like pizza a lot because it is fast and my favortite pizza is {pizzaTypes[1].title()}")

# 4-2
animals = ["lion", "tiger", "puma"]
for mammals in animals:
    print(f"{mammals.title()}, is one of the strongest mammals in the jungle")
print("Any of these animals are strong, violent yet gorgeous to look at")

# Making numerical lists
for i in range(1, 8):  # keep in mind a list always starts at index 0
    print(i)  # when printing it starts at value 1 which is at index 0 up to index 8 which has value 7
print()
for i in range(1, 9):  # prints the numbers from 1-8 instead of 1-9
    print(i)

# Using range() to make a list of numbers
numbers = list(range(1, 6))  # prints the number list values from 1-6 which is 1 to 6 as list starts at index 0
print(numbers)

evenNums = list(range(2, 11, 2))  # prints nums from 2 to 11 that are even
print(evenNums)

squares = []  # creates an empty list of squared values
for i in range(1, 11):
    # square= i ** 2 #squares all values from 1 to 10
    # squares.append(square) #stores each of these values in list
    # more concise we can use
    squares.append(i ** 2)
print(squares)

# simple statistics with list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# list comprehension
cubes = [i ** 3 for i in range(1, 11)]
print(cubes)

# 4-3 Counting to 20
for i in range(1, 21):
    print(i)

# 4-4 One million
oneToMillion = [i for i in range(1, 10001)]
# print(oneToMillion)
print(max(oneToMillion))
print(min(oneToMillion))
print(sum(oneToMillion))

# 4-6 odd numbers
nums = []
for i in range(1, 21, 2):
    nums.append(i)
print(nums)

# 4-7 threes
nums = []
for i in range(3, 30, 3):
    nums.append(i)
print(nums)

# 4-8 and 4-9 CUBES and Cube comprehension
cubes = [i ** 3 for i in range(1, 11)]
print(cubes)

# Working with part of a list
# SLicing a list
players = ["Diogo", "Sergio", "Fernando", "Alejandro", "Rohana"]
print(players[0:3])
print(players[3:5])
print(players[:4])  # ommiting first number is the same as starting from [0:4]
print(players[2:])  # ommiting second number is the same as displaying from start index to last element in list
print(players[-3:])  # displays last 3 elements of the list

#looping through a slice
print("here are the first 3 players of my team")
for player in players[:3]:
    print(player.title())

#COPYING A LIST
my_plates=["Strogof","Chipotle bowl", "Salad", "pasta"]
friends_plates= my_plates[:] #copies every element in list
print("My favorite plates are: ", my_plates)
print("My friends favorite plates are: ",friends_plates)

my_plates.append("pizza")
friends_plates.append("Cane's")
print(my_plates)
print(friends_plates)

print()
#4-10 Slices
print(my_plates)
print("The first 3 plates are: ", my_plates[0:3])
print("The in between plate is: ", my_plates[2:3])
print("The last 2 plates are: ", my_plates[-2:])

#4-11
sports=["football", "tennis", "basketball"]
print("Original list: ",sports)
addSports=sports[:]
print("Copied list: ",addSports)
sports.append("water polo")
print("Original list plus the new sport added: ",sports)

#TUPLES
dimensions=(100, 121)
print(dimensions[0])
print(dimensions[1])
#trying to change value of the tuple at index 1
#dimensions[1]=300 #because tuple is immutable we cannot change its value
#print(dimensions[1])

#To create a tuple with one element we always need a "," at the end of the element
#Example:
numberTuple=(3,)
#print(numberTuple[0])
print(numberTuple)

#looping over a tuple:
for i in dimensions:
    print(i)
#example

tuple=(500,200)
print("Original tuple is:")
for i in tuple:
    print(i)

tuple=(1,2)
print("The modified tuple is: ")
for i in tuple:
    print(i)
