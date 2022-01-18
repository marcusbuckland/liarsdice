from constants import Constants


class Bid:
    """ Represents a Bid in the game."""

    def __init__(self, quantity, value):
        self.quantity = quantity  # {1 -> n} where n is number of dice in play
        self.value = value  # {1, 2, 3, 4, 5, 6}

    def __repr__(self):
        return str(f"{Constants.QUANTITY_WORDS[self.quantity]} {Constants.DICE_WORDS_PLURAL[self.value]}")

    def __eq__(self, other):
        return self.quantity == other.quantity and self.value == other.value

    def __gt__(self, other):
        return self.get_equality_value() > other.get_equality_value()

    def __lt__(self, other):
        return self.get_equality_value() < other.get_equality_value()

    def get_quantity(self):
        return self.quantity

    def get_value(self):
        return self.value

    def is_ace_bid(self):
        return self.value == Constants.ACE_VALUE

    def not_ace_bid(self):
        return self.value != Constants.ACE_VALUE

    def get_equality_value(self):
        if self.is_ace_bid():
            return self.get_quantity() * 12 + 7
        # Not an ace bid
        return self.get_quantity() * 6 + self.get_value()
