# file counts the words of any txt file we give to the function

def countWords(fileName):
    try:
        with open(fileName, encoding='utf-8') as f:
            contents= f.read()
    except FileNotFoundError:
        #print(f"Sorry file {fileName} does not exist!")
        pass # if an error occurs we ignore that exception and continue to execute the program
    else:
        words= contents.split()
        num_words= len(words)
        print(f"The file {fileName} has {num_words} words!")

#call for only one file 
# filename='chpt10.txt'
# countWords(filename)

files= ['chpt10.txt','pi_digits.txt','programming.txt', 'Chpt8\Chpt8.txt']
for file in files:
    countWords(file)