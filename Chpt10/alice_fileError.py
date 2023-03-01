fileName='alice.txt'

# encoding ='utf-8' argument -> it is needed when the system's default encoding does not match the enconding of the file that is being read 
try: 
    with open(fileName, encoding='utf-8') as f: # same as file_object, its just a variable name
        contents =f.read()
except FileNotFoundError:
    print(f"File {fileName} does not exist")
