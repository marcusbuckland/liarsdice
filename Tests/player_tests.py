import math
import unittest
from player import Player
from player import is_valid_value
from bid import Bid


class PlayerTestCase(unittest.TestCase):
    def test_erroneous_bid_values(self):
        bid_value = 7
        self.assertFalse(is_valid_value(bid_value))

        bid_value = -8
        self.assertFalse(is_valid_value(bid_value))

        bid_value = math.pi
        self.assertFalse(is_valid_value(bid_value))

        bid_value = math.inf
        self.assertFalse(is_valid_value(bid_value))

        bid_value = -math.inf
        self.assertFalse(is_valid_value(bid_value))

        bid_value = math.tau
        self.assertFalse(is_valid_value(bid_value))

        bid_value = math.inf ** math.inf
        self.assertFalse(is_valid_value(bid_value))

    def test_bid_greater_than(self):
        big_bid = Bid(5, 2)
        small_bid = Bid(4, 2)
        self.assertGreater(big_bid, small_bid)


if __name__ == '__main__':
    unittest.main()
