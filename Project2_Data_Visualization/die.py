"""Class to create the die"""
""" A die needs to have 6 sides 
and it needs to roll as characteristics"""
from random import randint 
class Die:
    def __init__(self, num_sides=6):
        """Assuming its a 6 sided die"""
        self.num_sides=num_sides
    
    def roll(self):
        return randint(1, self.num_sides)
