"""file: die.py
this module defines the die class.
"""
from random import randint

class Die(object):
    """the class represents a six-sided die."""
    def __init__(self):
        """this initial face of the die."""
        self.value = 1

    def roll(self):
        """reset the die's value to a random number
between 1 and 6 """
        self._value = randint(1, 6)
        return self._value

    def getValue(self):
        return self._value

    def  __str__(self):
        return str(self._value)

print(Die().roll())
