from random import randint

class Die():
    """Representation of 1 dice"""
    def __init__(self, num_sides=6):
        """Default = 6 sided cube"""
        self.num_sides = num_sides
    
    def roll(self):
        """Return random value between 1 and num_sides"""
        return randint(1,self.num_sides)