from game import Game

class Main():
    def __main__(self):
        game = Game()
        game.generate_players()
        game.play_round()