from game import Game
import io

class TestTheGame:

    def test_can_create_game(self): 
        g = Game(["Bede", "Marcus"])
        assert g != None