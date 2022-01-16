from game import Game

if __name__ == '__main__':
    game = Game(player_names=['Marcus','Bede', 'Steph', 'Kim'], god_mode=True)
    round_counter = 1
    while game.not_finished():
        print("=============================")
        print(f"Round {round_counter}:")
        print("=============================")
        if game.is_god_mode():
            game.print_state()
        print(f"There are {game.get_dice_remaining_amount()} dice remaining.\n")
        round_counter += 1
        game.play_round()
    print(f"{game.get_remaining_players()[0].get_name()} is the winner!!")
