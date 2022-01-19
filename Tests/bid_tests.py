import math
import unittest
from bid import Bid
from constants import Constants


class BidTests(unittest.TestCase):
    def test_bid_gt(self):
        # Not ace v Not ace - same quantity
        gt = Bid(5, 6)
        lt = Bid(5, 2)
        self.assertGreater(gt, lt)

        # Not ace v Not ace - different quantity
        gt = Bid(6, 6)
        lt = Bid(5, 6)
        self.assertGreater(gt, lt)

        # Ace v Not ace
        gt = Bid(5, Constants.ACE_VALUE)
        lt = Bid(10, 6)
        self.assertGreater(gt, lt)

        # Not ace v Ace
        gt = Bid(10, 6)
        lt = Bid(2, Constants.ACE_VALUE)
        self.assertGreater(gt, lt)

        # Ace v Ace
        gt = Bid(10, Constants.ACE_VALUE)
        lt = Bid(9, Constants.ACE_VALUE)
        self.assertGreater(gt, lt)

    def test_bid_lt(self):
        # Not ace v Not ace - same quantity
        lt = Bid(10, 2)
        gt = Bid(10, 6)
        self.assertLess(lt, gt)

        # Not ace v Not ace - different quantity
        lt = Bid(1, 6)
        gt = Bid(2, 6)
        self.assertLess(lt, gt)

        # Ace v Not ace
        lt = Bid(5, Constants.ACE_VALUE)
        gt = Bid(11, 6)
        self.assertLess(lt, gt)

        # Not ace v Ace
        lt = Bid(4, 6)
        gt = Bid(8, Constants.ACE_VALUE)
        self.assertLess(lt, gt)

        # Ace v Ace
        lt = Bid(9, Constants.ACE_VALUE)
        gt = Bid(10, Constants.ACE_VALUE)
        self.assertLess(lt, gt)

    def test_bid_eq(self):
        # Not ace
        b1 = Bid(5, 5)
        b2 = Bid(5, 5)
        self.assertEqual(b1, b2)

        # Ace
        b1 = Bid(10, Constants.ACE_VALUE)
        b2 = Bid(10, Constants.ACE_VALUE)
        self.assertEqual(b1, b2)

    def test_repr(self):
        # Ace Bid
        bid = Bid(10, Constants.ACE_VALUE)
        self.assertEqual(bid.__repr__(), "Ten ones")

    def test_is_ace_bid_method(self):
        bid = Bid(10, Constants.ACE_VALUE)
        self.assertTrue(bid.is_ace_bid())

    def test_not_ace_bid_method(self):
        for value in range(2, 7):
            bid = Bid(10, value)
            self.assertTrue(bid.not_ace_bid())


if __name__ == '__main__':
    unittest.main()
