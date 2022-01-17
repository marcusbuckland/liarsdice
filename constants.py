class Constants:

    ACE_VALUE = 1
    ACE_PROBABILITY = 1/6 # The probability of rolling a 1 on a 6 sided die.
    NOT_ACE_PROBABILITY = 1/3 # The probability of rolling {2, 3, 4, 5, 6} on a 6 sided die when 1's are wild.

    quantity_words = dict(zip([i for i in range(0, 51)], ["Zero", "One", "Two", "Three", "Four", "Five", "Six",
                                                          "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                                                          "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                                                          "Eighteen", "Nineteen", "Twenty", "Twenty-one", "Twenty-two",
                                                          "Twenty-three", "Twenty-four", "Twenty-five", "Twenty-six",
                                                          "Twenty-seven", "Twenty-eight", "Twenty-nine", "Thirty",
                                                          "Thirty-one", "Thirty-two", "Thirty-three", "Thirty-four",
                                                          "Thirty-five", "Thirty-six", "Thirty-seven", "Thirty-eight",
                                                          "Thirty-nine", "Forty", "Forty-one", "Forty-two", "Forty-three",
                                                          "Forty-four", "Forty-five", "Forty-six", "Forty-seven", "Forty-eight",
                                                          "Forty-nine", "Fifty"]))

    dice_words = dict(zip([i for i in range(1, 7)], ["ones", "twos", "threes", "fours", "fives", "sixes"]))
    singular_dice_words = dict(zip([i for i in range(1, 7)], ["one", "two", "three", "four", "five", "six"]))

    valid_responses = ["bid", "b", "call", "c", "exactcall", "e", "quit", "q"]
    bid_responses = ["bid", "b"]
    call_responses = ["call", "c"]
    exactcall_responses = ["exactcall", "e"]
    quit_responses = ["quit", "q"]
    valid_bid_values = [i for i in range(1,7)]

    game_title = """
  _____     _____       _       _______     ______    ______   _____   ______  ________  
 |_   _|   |_   _|     / \     |_   __ \  .' ____ \  |_   _ `.|_   _|.' ___  ||_   __  | 
   | |       | |      / _ \      | |__) | | (___ \_|   | | `. \ | | / .'   \_|  | |_ \_| 
   | |   _   | |     / ___ \     |  __ /   _.____`.    | |  | | | | | |         |  _| _  
  _| |__/ | _| |_  _/ /   \ \_  _| |  \ \_| \____) |  _| |_.' /_| |_\ `.___.'\ _| |__/ | 
 |________||_____||____| |____||____| |___|\______.' |______.'|_____|`.____ .'|________| 
                                                                                         
"""
