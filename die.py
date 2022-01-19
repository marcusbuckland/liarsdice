import random


class Die:
    """Represents a die object."""

    def __init__(self, value=None):
        self.value = random.randint(1, 6) if value is None else value

    def __repr__(self):
        return str(self.value)

    def roll(self):
        """Rolls a six sided die."""
        self.value = random.randint(1, 6)
