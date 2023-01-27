prompt= "\nTell me something, and i will repeat it back to you"
prompt+= "\nEnter 'quit' to end the program: "

message=""
# this part will print quit back but it can be fixed with an 'if' statement where quit will not be printed
while message != 'quit':
    message= input(prompt)
    if message != 'quit':
        print(message)

