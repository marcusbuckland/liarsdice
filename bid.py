from constants import Constants


class Bid:
    """Represents a Bid in the game."""

    def __init__(self, quantity, value):
        """
        :param quantity: the quantity of the dice for that bid.
        :param value: the face value of the dice for that bid.
        """
        self.quantity = quantity  # {1 -> n} where n is number of dice in play
        self.value = value  # {1, 2, 3, 4, 5, 6}

    def __repr__(self):
        return str(f"{Constants.QUANTITY_WORDS[self.quantity]} {Constants.DICE_WORDS_PLURAL[self.value]}")

    def __eq__(self, other):
        return self.get_quantity() == other.get_quantity() and self.get_value() == other.get_value()

    def __gt__(self, other):
        return self.get_equality_value() > other.get_equality_value()

    def __lt__(self, other):
        return self.get_equality_value() < other.get_equality_value()

    def get_quantity(self):
        """Returns the quantity of the bid."""
        return self.quantity

    def get_value(self):
        """Returns the value of the bid- the face value of the dice for that bid."""
        return self.value

    def is_ace_bid(self):
        """Returns True if the bid is an Ace bid, False otherwise."""
        return self.value == Constants.ACE_VALUE

    def not_ace_bid(self):
        """Returns True if the bid isn't an Ace bid, False otherwise."""
        return self.value != Constants.ACE_VALUE

    def get_equality_value(self):
        """Returns the equality value of a bid, which is used to create a natural ordering of bids."""
        if self.is_ace_bid():
            return self.get_quantity() * 12 + 1
        # Not an ace bid
        return (self.get_quantity() - 1) * 6 + self.get_value()
