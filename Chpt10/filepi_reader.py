with open('pi_digits.txt') as file_object:
    contents= file_object.read()

print(contents.rstrip())

"""
Keyword "with"  closes the file once access to it is no longer needed, with keyword does not need to be used always
We called opne() method to open file
we can close it by diong close(), however if there is a bug that prevents the closing
method from executing the file may never close

Improperly closed files may cause data to be lost, deprecated or corrupted

rstrip() method removes any whitespace characters from right sid of a string

"""