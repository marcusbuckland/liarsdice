from game import Game
from constants import Constants

if __name__ == '__main__':
    print(Constants.GAME_TITLE)
    game = Game(player_names = ["Marcus", "Steph", "Bede", "Kim"], god_mode=True)
    round_counter = 1
    while game.not_finished():
        print("=============================")
        print(f"Round {round_counter}:")
        print("=============================")
        print(f"There are {game.get_dice_remaining_amount()} dice remaining.\n")
        round_counter += 1
        game.play_round()
    print(f"{game.get_remaining_players()[0].get_name()} is the winner!!")
