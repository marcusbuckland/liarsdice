import math
import unittest

from bid import Bid
from constants import Constants
from die import Die
from player import is_valid_value, is_valid_quantity, Player


class PlayerTests(unittest.TestCase):
    def test_invalid_bid_values(self):
        bid_value = '7'
        self.assertFalse(is_valid_value(bid_value))

        bid_value = '-1'
        self.assertFalse(is_valid_value(bid_value))

        bid_value = '0'
        self.assertFalse(is_valid_value(bid_value))

        bid_value = str(math.pi)
        self.assertFalse(is_valid_value(bid_value))

        bid_value = str(math.inf)
        self.assertFalse(is_valid_value(bid_value))

        bid_value = str(-math.inf)
        self.assertFalse(is_valid_value(bid_value))

        bid_value = str(math.tau)
        self.assertFalse(is_valid_value(bid_value))

        bid_value = str(math.inf ** math.inf)
        self.assertFalse(is_valid_value(bid_value))

    def test_valid_bid_values(self):
        for bid_value in range(1, 7):
            self.assertTrue(is_valid_value(str(bid_value)))

    def test_invalid_bid_quantities(self):
        bid_quantity = "one"
        self.assertFalse(is_valid_quantity(bid_quantity))

        bid_quantity = "two"
        self.assertFalse(is_valid_quantity(bid_quantity))

        bid_quantity = "three"
        self.assertFalse(is_valid_quantity(bid_quantity))

        bid_quantity = "four"
        self.assertFalse(is_valid_quantity(bid_quantity))

        bid_quantity = str(math.inf)
        self.assertFalse(is_valid_quantity(bid_quantity))

        bid_quantity = str(-math.inf)
        self.assertFalse(is_valid_quantity(bid_quantity))

        bid_quantity = "bid"
        self.assertFalse(is_valid_quantity(bid_quantity))

        bid_quantity = "call"
        self.assertFalse(is_valid_quantity(bid_quantity))

        bid_quantity = "exactcall"
        self.assertFalse(is_valid_quantity(bid_quantity))

        bid_quantity = "help"
        self.assertFalse(is_valid_quantity(bid_quantity))

    def test_lose_die(self):
        player = Player()
        player.lose_die()
        self.assertTrue(player.get_dice_quantity() == Constants.DICE_START_AMOUNT - 1)

    def test_gain_die(self):
        player = Player()
        player.gain_die()
        self.assertTrue(player.get_dice_quantity() == Constants.DICE_START_AMOUNT + 1)

    def test_has_gained_die(self):
        player = Player()
        self.assertFalse(player.get_has_gained_die())
        player.gain_die()
        self.assertTrue(player.get_has_gained_die())

    def test_hasnt_gained_die(self):
        player = Player()
        self.assertTrue(player.hasnt_gained_die())
        player.gain_die()
        self.assertFalse(player.hasnt_gained_die())

    def test_has_lost(self):
        player = Player()
        for _ in range(Constants.DICE_START_AMOUNT):
            player.lose_die()
        self.assertTrue(player.has_lost())

    def test_is_remaining(self):
        player = Player()
        self.assertTrue(player.is_remaining())

    def test_get_amount(self):
        dice = [Die(2), Die(3), Die(3), Die(3), Die(5)]
        player = Player(dice=dice)

        bid = Bid(3, 3)
        self.assertTrue(player.get_amount(bid) == 3)

        bid = Bid(5, 2)
        self.assertTrue(player.get_amount(bid) == 1)

        bid = Bid(4, 1)
        self.assertTrue(player.get_amount(bid) == 0)

    def test_roll(self):
        # TODO Re-write this test utilising a random seed.
        player = Player()
        original_dice = sorted(player.get_dice_values())
        for _ in range(10):
            player.roll()
            rolled_dice = sorted(player.get_dice_values())
            if original_dice != rolled_dice:
                self.assertTrue(original_dice != rolled_dice)










if __name__ == '__main__':
    unittest.main()
