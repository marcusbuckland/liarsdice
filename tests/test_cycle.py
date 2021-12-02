from game import Game
from bid import Bid
import io


class TestTheGame:

    def test_can_create_game(self):
        g = Game(player_names=["Bede", "Marcus"])
        assert g is not None

    def test_bid_equality(self):
        b1 = Bid(1, 1)
        b2 = Bid(1, 1)
        assert b1 == b2

    def test_bid_01(self):
        b1 = Bid(5, 4)
        b2 = Bid(6, 4)
        assert b1 < b2

    def test_bid_02(self):
        b1 = Bid(5, 4)
        b2 = Bid(6, 4)
        assert not b1 > b2

    def test_bid_03(self):
        b1 = Bid(3, 3)
        b2 = Bid(1, 1)
        assert b1 > b2

    def test_bid_04(self):
        b1 = Bid(3, 3)
        b2 = Bid(2, 1)
        assert b2 > b1



