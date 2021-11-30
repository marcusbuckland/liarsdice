import random

class Die:
    """ Represents a die object."""
    def __init__(self, value=None):
        self.value = value

    def __repr__(self):
        return str("Die: " + str(self.value))

    def roll(self):
        self.value = random.randint(1, 6)
