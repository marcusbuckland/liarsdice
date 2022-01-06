from die import Die
from bid import Bid


class Player:
    """ Represents a player in the game."""

    def __init__(self, name):
        self.name = name
        self.dice = [Die() for _ in range(5)]

    def __repr__(self):
        return_string = ""
        return_string += self.name + " "
        return_string += str([d.value for d in self.dice])
        return return_string

    def get_name(self):
        return self.name

    def get_dice(self):
        return self.dice

    def get_dice_values(self):
        return [d.value for d in self.dice]

    def roll(self):
        for die in self.dice:
            die.roll()

    def lose_die(self):
        self.dice.pop()

    def gain_die(self):
        self.dice.append(Die())

    def bid(self, previous_bid=None):
        # Maybe a try/except to stop erroneous bids (e.g. someone bid's a string etc)        

        # Create bid
        quantity = int(input("Bid quantity: "))
        value = int(input("Bid value: "))
        bid = Bid(quantity, value)

        # Beginning of a bidding round, no previous bid
        if previous_bid is None:
            return bid

        if bid > previous_bid:
            return bid
        else:
            # Bid was too low- make another bid.
            return self.bid(previous_bid)

    def has_lost(self):
        return not self.dice

    def is_remaining(self):
        return bool(self.dice)
