
prompt="Tell me something and i will repeat: "
active = True #variable takes true as a boolean
while active:
    message= input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)