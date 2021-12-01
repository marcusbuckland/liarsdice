from game import Game





if __name__ == '__main__':
    game = Game()
    round_counter = 1
    while not(game.is_finished()):
        print(f"ROUND {round_counter}")
        round_counter+=1
        game.play_round()
        print(game)

