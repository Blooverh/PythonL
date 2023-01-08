firstName ="Diogo"
lastName = "Aires"
fullName = f"{firstName} {lastName}" # f-strings -> f is used for format
#print(fullName)
print(f"hello, {fullName.title()} !")
#white spaces
print("\tpython")
print("Languages:\npython\njava\nC++")

message= "One of Python's strengths is community"
print(message)

#Ints and floats 
#   * for multiplication
#   ** for exponents 

multiplication= 2*3
print(multiplication)
exponent= 2**3 
print(exponent)

#mixing a float with an integer always gives a float result
equation = 2 * (3.5**2.2)
print(equation)

#declaring long numbers we use underscore(_)
longNum= 14_000_000_000
print(longNum)

#multiple assignment 

x,y,z= 1,2,3
print(x)
print(y)
print(z)
print(z,x,y)

#Python does not have built in librabry for constants (variables who do not change their value the entire program)
#but we can let it know by assigning the variable in CAPITAL LETTERS 

EXAMPLE_CONSTANT = 2000
print(EXAMPLE_CONSTANT)
