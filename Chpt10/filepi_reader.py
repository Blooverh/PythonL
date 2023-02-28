filename='pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        

"""
Keyword "with"  closes the file once access to it is no longer needed, with keyword does not need to be used always
We called opne() method to open file
we can close it by diong close(), however if there is a bug that prevents the closing
method from executing the file may never close

Improperly closed files may cause data to be lost, deprecated or corrupted

rstrip() method removes any whitespace characters from right sid of a string

"""