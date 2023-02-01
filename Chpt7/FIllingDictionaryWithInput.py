responses={} #empty dictionary

polling_active=True

while polling_active:
    name=input("Enter first name: ")
    response=input("What is your favorite country? ")
    responses[name]= response
    repeat= input("Would you like to let another person respond? (yes/no)")
    if repeat== 'no':
        polling_active=False


print("\n---POLL RESULTS---")
for name, response in responses.items():
    print(f"{name}'s favorite country is {response}")

        