from game import Game

if __name__ == '__main__':
    game = Game(['Marcus','Bede'])
    round_counter = 1
    while game.not_finished():
        print("=============================")
        print(f"Round {round_counter}:")
        print("=============================")
        round_counter += 1
        game.play_round()
        # print(game)
    print(f"{game.get_remaining_players()[0].get_name()} is the winner!!")
