#input() function

message= input("Tell me your name and i will repeat to you: ")
print(message)

nums=[4,3,2,4,1]

name= input("Enter your name: ")
print(f"Hello {name} ! Welcome friend!")

#add extra lines to a prompt

prompt="If you tell us who you are, we can personalize the messages you see."
prompt+="\nWhat is your name: "
name=input(prompt)
print(f"{name}, hello kind sir. ")

#Using int() to accept numerical input
age= input("How old are you? ")
age=int(age)
print(f"Your age is {age}!")
if age >=18:
    print("You are considered an adult in every country in the world!")


#MODULO OPERATOR (%)
#returns the remainder of a division between 2 numbers

remainder= 4%3
print(remainder)

#Even or odd nums
number= input("ENter a number to check if its even or odd: ")
number=int(number)

if number %2 ==0:
    print(f"number {number} is even.")
else:
    print(f"number {number} is odd")


#Exercise 7-3 multiples of 10

number= input("ENter a number to check if its a multiple of 10.")
number= int(number)
if number %10 ==0:
    print(f"{number} is a multiple of 10")
else:
    print(f"{number} is not a multiple of 10")

#WHILE LOOPS

current=1
while current <= 5:
    print(current)
    current+=1

#Allowing user to choose when to quit
