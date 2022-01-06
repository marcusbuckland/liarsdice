import random


class Die:
    """ Represents a die object."""

    def __init__(self):
        self.value = random.randint(1, 6)

    def __repr__(self):
        return str(self.value)

    def roll(self):
        self.value = random.randint(1, 6)
