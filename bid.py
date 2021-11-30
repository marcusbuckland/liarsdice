from constants import Constants

class Bid:
    """ Represents a Bid in the game."""
    def __init__(self, quantity, value) :
        self.quantity = quantity # {1 -> n} where n is number of dice in play
        self.value = value # {1, 2, 3, 4, 5}

    def __repr__(self) :
        return str(f"{Constants.quantity_words[self.quantity]} {Constants.dice_words[self.value]}")

    def __eq__(self, other) :
        return self.quantity == other.quantity and self.value == other.value

    def __gt__(self, other):
        if self.not_ace_bid() and other.not_ace_bid() :
            if self.quantity == other.quantity :
                return self.value > other.value
            else :
                return self.quantity > other.quantity
        if self.is_ace_bid() and other.not_ace_bid() : 
            return self.quantity * 2 >= other.quantity
        if self.not_ace_bid() and other.is_ace_bid() : 
            return self.quantity > other.quantity * 2
        if self.is_ace_bid() and other.is_ace_bid() :
            return self.quantity > other.quantity

    def __lt__(self, other):
        if self.not_ace_bid() and other.not_ace_bid() : 
            if self.quantity == other.quantity :
                return self.value < other.value
            else :
                return self.quantity < other.quantity
        if self.is_ace_bid() and other.not_ace_bid() : 
            return self.quantity * 2 <= other.quantity
        if self.not_ace_bid() and other.is_ace_bid() :
            return self.quantity < other.quantity * 2
        if self.is_ace_bid() and other.is_ace_bid() :
            return self.quantity < other.quantity

    def is_ace_bid(self):
        return self.value == 1

    def not_ace_bid(self):
        return self.value != 1