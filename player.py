from die import Die
from bid import Bid
from constants import Constants

def is_valid_value(value):
    """
    :param value: value of dice to be checked
    :return: True if the value is a valid dice value, False otherwise.
    """
    if value.isnumeric():
        return int(value) in Constants.VALID_BID_VALUES
    return False

def is_valid_quantity(quantity):
    """
    :param quantity: quantity of the bid to be checked
    :return: True if the quantity is a valid bid quantity, False otherwise.
    """
    return quantity.isnumeric()

class Player:
    """ Represents a player in the game."""

    def __init__(self, name="player", dice=None, has_gained_die=False, has_been_blind=False):
        self.name = name
        self.dice = [Die() for _ in range(Constants.DICE_START_AMOUNT)] if dice is None else dice
        self.has_gained_die = has_gained_die
        self.has_been_blind = has_been_blind

    def __repr__(self):
        return_string = ""
        return_string += self.name + ": "
        return_string += str(self.get_dice_values())
        return return_string

    def get_name(self):
        return self.name

    def get_dice(self):
        return self.dice

    def get_has_gained_die(self):
        return self.has_gained_die

    def hasnt_gained_die(self):
        return not self.has_gained_die

    def get_has_been_blind(self):
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

    def bid(self, previous_bid=None, quantity=None, value=None):
        """
        :param previous_bid:
        :param quantity:
        :param value:
        :return:
        """
        while quantity is None:
            quantity = input("Bid quantity: ")
            if not is_valid_quantity(quantity):
                print("Input a valid quantity!")
                quantity = None
            else:
                quantity = int(quantity)

        while value is None:
            value = input("Bid value: ")
            if not is_valid_value(value):
                print("Input a valid value: can be one of {1, 2, 3, 4, 5, 6}")
                value = None
            else:
                value = int(value)
        # Create bid
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
