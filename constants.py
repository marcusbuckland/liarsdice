class Constants:

    ACE_VALUE = 1
    ACE_PROBABILITY = 1/6 # The probability of rolling a 1 on a 6 sided die.
    NOT_ACE_PROBABILITY = 1/3 # The probability of rolling {2, 3, 4, 5, 6} on a 6 sided die when 1's are wild.
    DICE_START_AMOUNT = 5

    QUANTITY_WORDS = dict(zip([i for i in range(0, 51)], ["Zero", "One", "Two", "Three", "Four", "Five", "Six",
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
    DICE_WORDS_PLURAL = dict(zip([i for i in range(1, 7)], ["ones", "twos", "threes", "fours", "fives", "sixes"]))
    DICE_WORDS_SINGULAR = dict(zip([i for i in range(1, 7)], ["one", "two", "three", "four", "five", "six"]))

    VALID_RESPONSES = {"bid", "b", "call", "c", "exactcall", "e", "help", "h", "quit", "q"}
    BID_RESPONSES = {"bid", "b"}
    CALL_RESPONSES = {"call", "c"}
    EXACTCALL_RESPONSES = {"exactcall", "e"}
    HELP_RESPONSES = {"help", "h"}
    QUIT_RESPONSES = {"quit", "q"}
    VALID_BID_VALUES = set(range(1, 7))

    GAME_TITLE = """
  _____     _____       _       _______     ______    ______   _____   ______  ________  
 |_   _|   |_   _|     / \     |_   __ \  .' ____ \  |_   _ `.|_   _|.' ___  ||_   __  | 
   | |       | |      / _ \      | |__) | | (___ \_|   | | `. \ | | / .'   \_|  | |_ \_| 
   | |   _   | |     / ___ \     |  __ /   _.____`.    | |  | | | | | |         |  _| _  
  _| |__/ | _| |_  _/ /   \ \_  _| |  \ \_| \____) |  _| |_.' /_| |_\ `.___.'\ _| |__/ | 
 |________||_____||____| |____||____| |___|\______.' |______.'|_____|`.____ .'|________| 
                                                                                         
"""
