import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase): #class that will contain a series of unit tests for get_formatted_name() function
    """ Test for 'name_function.py """

    def test_first_last_name(self):
        """Do name's like Janis Joplin work ?"""

        formatted_name= get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin') # ASSERT METHODS -> verify that a result we received matches the result we expected to receive 

#__name__ set when the program is executed.
#if this file is being run as the main program, the value of __name__ is set to __main__
if __name__ == '__main__': 
    unittest.main() # runs the test case