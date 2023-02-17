#Arbitrary number of arguments
# The asterisk in the parameter name *toppings tells Python to make an 
#   empty tuple called toppings and pack whatever values it receives into this tuple.
def make_pizza(size,*toppings):
    print(f"Making a {size}-inch pizza with the following topics: ")
    for topping in toppings:
        print(topping)

# make_pizza(14,'peperonni')
# print()
# make_pizza(12,'mushrooms','green peppers', 'extra cheese')