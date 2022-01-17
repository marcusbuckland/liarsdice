import math
import unittest
from player import is_valid_value


class PlayerTests(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
