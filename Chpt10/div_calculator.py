print("Give me 2 numbers, and i'll divide them: ")
print("Enter 'q' to quit. ")

while True:
    firstNum= input("Enter 1st number: ")

    if firstNum == 'q':
        break

    secondNum= input("Enter 2nd number: ")
    if secondNum =='q':
        break
    # elif secondNum == 0:
    #     print("Cannot divide a number by zero")
    #     break
    try:
        answer= int(firstNum) / int(secondNum)
    except ZeroDivisionError:
        print("Second number cannot be 0 as we cannot divide a number by 0")
    else:
        print(f"Answer is: {answer}")