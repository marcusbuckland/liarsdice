from die import Die
from bid import Bid


class Player:
    """ Represents a player in the game."""

    def __init__(self, name):
        self.name = name
        self.dice = [Die() for _ in range(5)]
        self.has_gained_die = False
        self.has_been_blind = False

    def __repr__(self):
        return_string = ""
        return_string += self.name + ": "
        return_string += str([d.value for d in self.dice])
        return return_string

    def get_name(self):
        return self.name

    def get_dice(self):
        return self.dice

    def has_gained_die(self):
        return self.has_gained_die

    def hasnt_gained_die(self):
        return not self.has_gained_die

    def has_been_blind(self):
        return self.has_been_blind

    def hasnt_been_blind(self):
        return not self.has_been_blind

    def get_dice_values(self):
        return [d.value for d in self.dice]

    def roll(self):
        for die in self.dice:
            die.roll()

    def lose_die(self):
        self.dice.pop()

    def gain_die(self):
        self.has_gained_die = True
        self.dice.append(Die())

    def bid(self, previous_bid=None, quantity=None):
        # TODO better error handling of bids.
        # Create bid
        if quantity is None:
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
            print("Bid must be higher than previous bid!")
            return self.bid(previous_bid)

    def has_lost(self):
        return not self.dice

    def is_remaining(self):
        return bool(self.dice)

    def get_amount(self, bid):
        dice_values = self.get_dice_values()
        amount = dice_values.count(1)
        return amount if bid.is_ace_bid() else amount + dice_values.count(bid.get_value())

    def get_dice_quantity(self):
        return len(self.dice)

