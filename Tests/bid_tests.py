import math
import unittest
from bid import Bid
from constants import Constants


class BidTests(unittest.TestCase):
    def test_bid_gt(self):
        # Test bid quantity
        big = Bid(math.inf, 6)
        small = Bid(-math.inf, 6)
        self.assertGreater(big, small)

        # Test bid quantity
        big = Bid(30, 5)
        small = Bid(29, 5)
        self.assertGreater(big, small)

        # Test bid quantity
        big = Bid(2, 2)
        small = Bid(1, 2)
        self.assertGreater(big, small)

        # Test bid value
        big = Bid(math.inf, math.inf)
        small = Bid(math.inf, -math.inf)
        self.assertGreater(big, small)

        # Test bid value
        big = Bid(-math.inf, math.inf)
        small = Bid(-math.inf, -math.inf)
        self.assertGreater(big, small)

        # Test bid value
        big = Bid(math.inf, 6)
        small = Bid(math.inf, 2)
        self.assertGreater(big, small)

        # Test bid value
        big = Bid(10, 3)
        small = Bid(10, 2)
        self.assertGreater(big, small)

        # Test ace bid is smaller
        big = Bid(5, 2)
        small = Bid(2, Constants.ACE_VALUE)
        self.assertGreater(big, small)

        # Test ace bid is larger
        big = Bid(3, Constants.ACE_VALUE) # Ace
        small = Bid(5, 2)
        self.assertGreater(big, small)

    def test_bid_lt(self):
        # Test quantity.
        small = Bid(-math.inf, 6)
        big = Bid(math.inf, 6)
        self.assertGreater(big, small)









if __name__ == '__main__':
    unittest.main()
