fileName="programming.txt"

# 'w' in open method tells python the file we are opening is is on "writing mode", allowing us to write to code 
with open(fileName, 'w') as file_object:
    file_object.write("I love programming with Python.")# does not write string to a new line 
    file_object.write("I love flash.\n")# does write the next string to a new line
    file_object.write("Flash loves me.") 

with open(fileName, 'a') as file_object:
    file_object.write("\nHello its me my friend")