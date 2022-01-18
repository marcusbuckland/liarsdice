import random
from itertools import cycle
from bid import Bid
from player import Player
from call import Call
from exactcall import ExactCall
from constants import Constants
from collections import Counter

def factorial(n):
    """Returns the factorial of a number"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def binomial_coefficient(n, k):
    """Returns the number of combinations of choosing k from n"""
    return factorial(n) / (factorial(n - k) * factorial(k))

def binomial_pmf(k, n, p):
    """Returns the probability mass function of the Binomial Distribution
    P(X = k | n,p) where X ~ Bin(n, p)"""
    return binomial_coefficient(n, k) * p**k * (1-p)**(n-k)

def binomial_cdf(k, n, p, lower_tail=True):
    """Returns the cumulative distribution function of the Binomial Distribution
    P(X <= k | n,p) where X ~ Bin(n, p) """
    prob = sum([binomial_pmf(i, n, p) for i in range(0, k+1)])
    return prob if lower_tail else (1-prob)

def get_probability(bid, n, responder):
    """Returns the probability of a Bid's success."""
    k = bid.get_quantity() - responder.get_amount(bid)
    if k < 1 : return 1.00 # If responder has at least the quantity of dice of the bid then 100% chance of bid success.
    if k > n : return 0.00 # If k is larger than n, something has gone very wrong...
    p = Constants.ACE_PROBABILITY if bid.is_ace_bid() else Constants.NOT_ACE_PROBABILITY
    return binomial_cdf(k-1, n, p, lower_tail=False)

def generate_players(player_names=None):
    """This function creates the Player objects that will be playing the Game."""
    players = []
    if player_names:
        # Useful for creating games without user input (e.g tests).
        players = [Player(name) for name in player_names]
    else:
        num_players = int(input("How many players are playing?"))
        # Create the Player objects and store them inside players list
        for _ in range(num_players):
            name = input("Player's name?")
            players.append(Player(name))
    return players

def get_response():
    """This function returns a String that must be present in Constants.valid_responses or numeric.
    It is used to get a Player's response to a bid."""
    while True:
        response_string = input("How do you respond? (can be 'Bid', Call', or 'ExactCall'): ").lower()
        if response_string in Constants.VALID_RESPONSES:
            return response_string
        elif response_string.isnumeric():
            return response_string
        else:
            print(f"{response_string} is not a valid response!")
            continue

def clear_text():
    """Outputs 25 blank lines"""
    print("\n"*25)

def faceoff(bidder, bid, responder, unknown_dice_quantity, blind_round, blind_bidder):
    """
    A face-off occurs after bid has been made and must be responded to.
    They can respond with either a Bid of higher value, a Call, or ExactCall.
    :param bidder: The player that has made the current bid.
    :param bid: The curent bid.
    :param responder: The player that must respond to the current bid.
    :param unknown_dice_quantity: The amount of dice remaining in the game, less the amount of dice in the responder's set.
    :param blind_round: True if this round is a blind round, otherwise False.
    :param blind_bidder: The player who started the blind round if it's a blind round, otherwise None.
    :return:
    """
    clear_text()
    print(f"{bidder.get_name()} has made a bid of: {bid}.")
    if not blind_round:
        print(f"{responder.get_name()} you rolled: {responder.get_dice()}")
        print(
            f"The expected value of {bid} given your set of dice is {get_expected_value(responder, bid, unknown_dice_quantity):.2f}")
        print(
            f"The probability of this bid being successful is: {get_probability(bid, unknown_dice_quantity, responder):.4f}")
    else:
        if responder is not blind_bidder:
            print(f"{responder.get_name()} cannot look at their dice. This round is blind!")
        else:
            print(f"{responder.get_name()} you rolled: {responder.get_dice()}")

    response_string = get_response()

    # Bid response with String
    if response_string in Constants.BID_RESPONSES:
        response_bid = responder.bid(previous_bid=bid)
        return response_bid

    # Bid response with numeric
    if response_string.isnumeric():
        quantity = int(response_string)
        response_bid = responder.bid(previous_bid=bid, quantity=quantity)
        return response_bid

    # Call response
    if response_string in Constants.CALL_RESPONSES:
        return Call(bidder=bidder, bid=bid, caller=responder)

    # ExactCall response
    if response_string in Constants.EXACTCALL_RESPONSES:
        return ExactCall(bidder=bidder, bid=bid, caller=responder)

    # Quit response
    if response_string in Constants.QUIT_RESPONSES:
        exit()

    # Shouldn't reach here..


def get_expected_value(responder, bid, unknown_dice_quantity):
    """Returns the expected value of a bid value given a responder knows the quantity of that bid value
    for their own set of dice."""
    expected = responder.get_amount(bid)
    expected += unknown_dice_quantity * Constants.ACE_PROBABILITY if bid.is_ace_bid() \
        else unknown_dice_quantity * Constants.NOT_ACE_PROBABILITY
    return expected


class Game:
    """ Represents an actual instance of the game Liar's Dice (Dudo).
    https://en.wikipedia.org/wiki/Dudo"""

    def __init__(self, player_names=None, god_mode=False):
        self.players = generate_players(player_names)
        self.get_player_order()
        self.player_cycle = cycle(self.players)
        self.first_to_act = self.get_next_player()
        self.god_mode = god_mode

    def __repr__(self):
        return_str = ""
        for player in self.players:
            return_str += str(player) + "\n"
        return return_str

    def is_god_mode(self):
        return self.god_mode

    def print_state(self):
        for p in self.players:
            print(p)
        print("")
        counts = Counter(self.get_all_dice_values())
        for i in range(1, 7):
            if i == 1:
                print(f"{Constants.DICE_WORDS_PLURAL[i]}: {counts[i]}")
            else:
                print(f"{Constants.DICE_WORDS_PLURAL[i]}: {counts[1] + counts[i]} ({counts[i]})")
        print("")


    def get_player_order(self):
        """Each player rolls a die to determine the order of play- The Highest roll starts first.
        If players roll the same value, a re-roll occurs until the tie is broken."""
        sorted_players = []
        order = [[player, random.randint(1, 6)] for player in self.players]
        sorted_order = sorted(order, key=lambda elem: elem[1], reverse=True)
        while sorted_order:
            if len(sorted_order) > 1:
                p1_roll = sorted_order[0][1]
                p2_roll = sorted_order[1][1]
                if p1_roll != p2_roll:
                    sorted_players.append(sorted_order.pop(0)[0])
                    continue
                else:
                    # Re-roll to break the tie.
                    p1_reroll = random.randint(1, 6)
                    p2_reroll = random.randint(1, 6)
                    if p1_reroll != p2_reroll:
                        idx = 0 if p1_reroll > p2_reroll else 1
                        sorted_players.append(sorted_order.pop(idx)[0])
                        continue

            else:
                # Only one player left.
                sorted_players.append(sorted_order.pop()[0])

        self.players = sorted_players

    def is_finished(self):
        """True if the game is finished."""
        return self.players_remaining() <= 1

    def not_finished(self):
        """True if the game is not finished."""
        return not self.is_finished()

    def get_players(self):
        """Returns all players in the game."""
        return self.players

    def get_remaining_players(self):
        """Return all players that still have Dice remaining."""
        return list(filter(lambda x: bool(x.get_dice()) is not False, self.players))

    def get_first_to_act(self):
        """Returns the Player that is first to act in a round"""
        return self.first_to_act

    def players_remaining(self):
        """Returns the number of players still playing"""
        num_remaining = 0
        for player in self.players:
            if player.is_remaining():
                num_remaining += 1
        return num_remaining

    def get_next_player(self):
        """Returns the Player that will be next to act"""
        next_player = next(self.player_cycle)
        if next_player.is_remaining():
            return next_player
        else:
            return self.get_next_player()

    def all_players_roll_dice(self):
        """Every player in the game with dice left will roll.
        Used at the beginning of a round."""
        for player in self.players:
            player.roll()

    def reset_cycle(self):
        """Gets the player_cycle to the appropriate position."""
        while next(self.player_cycle) is not self.first_to_act:
            continue

    def play_round(self):
        """Plays a single round of Liar's Dice"""
        self.all_players_roll_dice()
        blind_round = False
        blind_bidder = None

        if self.god_mode:
            self.print_state()

        bidder = self.first_to_act

        # Check if it's a blind round
        if len(bidder.get_dice()) == 1 and bidder.hasnt_been_blind():
            bidder.has_been_blind = True
            blind_bidder = bidder
            blind_round = True

        print(f"{bidder.get_name()} must make a bid!")
        print(f"{bidder.get_name()} you rolled: {bidder.get_dice()}")
        bid = bidder.bid()

        # Ensure that self.player_cycle is set to the position of bidder so that responder is
        # correct player after get_next_player() called.
        self.reset_cycle()

        responder = self.get_next_player()

        # response is either Bid, Call, or ExactCall object
        unknown_dice_quantity = self.get_unknown_dice_quantity(responder)
        response = faceoff(bidder, bid, responder, unknown_dice_quantity, blind_round, blind_bidder)

        # Repeatedly have face-offs until a Call or ExactCall response
        while isinstance(response, Bid):
            bidder, responder = responder, self.get_next_player()
            unknown_dice_quantity = self.get_unknown_dice_quantity(responder)
            response = faceoff(bidder, response, responder, unknown_dice_quantity, blind_round, blind_bidder)

        # Call or ExactCall response- resolve and end round.
        self.resolve_call(response)

    def resolve_call(self, call):
        """Check which player won the face-off after a Call response."""
        bidder = call.get_bidder()
        bid = call.get_bid()
        caller = call.get_caller()
        bid_quantity = bid.get_quantity()
        bidder_possessive = str(bidder.get_name()+"'s") if bidder.get_name()[-1] != 's' else str(bidder.get_name()+"'")


        if isinstance(call, ExactCall):
            print(f"{caller.get_name()} has made an ExactCall against {bidder_possessive} bid of {bid}\n")
        else:
            print(f"{caller.get_name()} has called {bidder_possessive} bid of {bid}\n")

        for player in self.get_remaining_players():
            print(player)
            bid_value = Constants.DICE_WORDS_PLURAL[bid.get_value()] if player.get_amount(bid) != 1 \
                else Constants.DICE_WORDS_SINGULAR[bid.get_value()]
            amount = Constants.QUANTITY_WORDS[player.get_amount(bid)].lower()
            print(f"{player.get_name()} has {amount} {bid_value}\n")

        quantity = self.get_quantity(bid)
        quantity_str = Constants.QUANTITY_WORDS[quantity]

        if isinstance(call, ExactCall):
            if quantity != 1:
                print(f"There were exactly {quantity_str.lower()} {Constants.DICE_WORDS_PLURAL[bid.get_value()]} in that round.")
            else:
                print(f"There was exactly one {Constants.DICE_WORDS_SINGULAR[bid.get_value()]} in that round.")
            if quantity == bid_quantity:
                # caller won the ExactCall
                print(f"{caller.get_name()} won their ExactCall bid!")

                # players are only eligible to gain a die back once per game.
                if caller.hasnt_gained_die():
                    print(f"{caller.get_name()} gains a die.")
                    caller.gain_die()
                else:
                    print(f"{caller.get_name()} was ineligible to gain a die.")
                print(f"{bidder.get_name()} loses a die.\n")
                bidder.lose_die()
                self.first_to_act = bidder
            else:
                # caller lost the ExactCall
                print(f"{caller.get_name()} lost their ExactCall and loses a die.\n")
                caller.lose_die()

                # Was caller just eliminated from game?
                if caller.is_remaining():
                    self.first_to_act = caller
                else:
                    print(f"{caller.get_name()} has no dice remaining and is eliminated from the game!\n")
                    self.first_to_act = self.get_next_player()
        else:
            if quantity != 1:
                print(f"There were {quantity_str.lower()} {Constants.DICE_WORDS_PLURAL[bid.get_value()]} in that round.")
            else:
                print(
                    f"There was {quantity_str.lower()} {Constants.DICE_WORDS_SINGULAR[bid.get_value()]} in that round.")

            # response is just a regular Call
            if quantity >= bid_quantity:
                # bidder won & caller lost.
                print(f"{bidder.get_name()} won their bid of {bid}- {caller.get_name()} loses a die!\n")
                caller.lose_die()

                # Was caller just eliminated from game?
                if caller.is_remaining():
                    self.first_to_act = caller
                else:
                    print(f"{caller.get_name()} has no dice remaining and is eliminated from the game!\n")
                    self.first_to_act = self.get_next_player()
            else:
                # caller won & bidder lost.
                print(f"{bidder.get_name()} lost their bid of {bid} and loses a die.\n")
                bidder.lose_die()

                # Was bidder just eliminated from game?
                if bidder.is_remaining():
                    self.first_to_act = bidder
                else:
                    print(f"{bidder.get_name()} has no dice remaining and is eliminated from the game!\n")
                    self.first_to_act = caller

    def get_all_dice_values(self):
        """Returns a list of every dice value (int) that was rolled in that round."""
        dice_values = []
        for player in self.players:
            dice_values += player.get_dice_values()
        return dice_values

    def get_quantity(self, bid):
        """Returns the quantity of dice that count for a bid."""
        values = self.get_all_dice_values()
        quantity = values.count(1)  # 1's count as everything.
        return quantity if bid.is_ace_bid() else quantity + values.count(bid.get_value())

    def get_dice_remaining_amount(self):
        """Returns the quantity of dice that remain."""
        return len(self.get_all_dice_values())

    def get_unknown_dice_quantity(self, player):
        """Returns the quantity of dice held by players other than 'player'."""
        return self.get_dice_remaining_amount() - player.get_dice_quantity()