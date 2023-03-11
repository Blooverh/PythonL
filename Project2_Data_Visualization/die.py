"""Class to create the die"""
""" A die needs to have 6 sides 
and it needs to roll as characteristics"""
from random import randint 
class Die:
    #Takes optional argument since if no argument is included default value of sides of the die is 6, but we can change to 8
    def __init__(self, num_sides=6):
        """Assuming its a 6 sided die"""
        self.num_sides=num_sides
    
    #Randint method to obtain an random integer between 1 and the number of sides of the die
    def roll(self): 
        return randint(1, self.num_sides)
