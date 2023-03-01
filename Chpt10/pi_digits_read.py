fileName='pi_digits.txt'

with open(fileName) as fileObject:
    lines= fileObject.readlines()

pi_String=""

# works with contents of the file outisde of the 'with' block
for line in lines:
    # pi_String += line.rstrip() # -> creates white space between the numbers that are on each line and counts them in len() method
    pi_String += line.strip() #-> no Whitespaces exist

print(pi_String)
print(F"Length of the string is {len(pi_String)} numbers")
