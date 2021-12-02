import random
from itertools import cycle
from bid import Bid
from player import Player
from call import Call
from exactcall import ExactCall


def generate_players():
    """This function creates the Player objects that will be playing the Game."""
    num_players = int(input("How many players are playing?"))
    players = []

    # Create the Player objects and store them inside players list
    for i in range(num_players):
        name = input("Player's name?")
        players.append(Player(name))
    return players


def get_response():
    """This function returns a response string of 'Bid', 'Call', or 'ExactCall'.
    It is used to get a Player's response after a bid has been made."""
    valid_responses = ["Bid", "Call", "ExactCall"]
    while True:
        response_string = input("Response: ")
        if response_string in valid_responses:
            return response_string
        else:
            print("Invalid response!")
            print("Choose one of 'Bid', 'Call', or 'ExactCall'")
            continue


def faceoff(bidder, bid, responder):
    """A faceoff is effectively when a bid has been made and it is time for the responder to play.
    They can respond with a Bid of higher value, or make a Call or ExactCall (which would end that round)."""
    print(f"{bidder.get_name()} has made a bid of: {bid}.")
    print(f"{responder.get_name()} is responding to {bidder.get_name()}'s bid...")

    response_string = get_response()

    # Bid
    if response_string == "Bid":
        response_bid = responder.bid(previous_bid=bid)
        print(f"{responder.get_name()} responds with a bid of: {response_bid}")
        return response_bid

    # Call
    if response_string == "Call":
        return Call(bidder=bidder, bid=bid, caller=responder)

    # ExactCall
    if response_string == "ExactCall":
        return ExactCall(bidder=bidder, bid=bid, caller=responder)


class Game:
    """ Represents an actual instance of the game Liar's Dice (Dudo).
    https://en.wikipedia.org/wiki/Dudo"""

    def __init__(self):
        self.players = generate_players()
        self.get_player_order()
        self.player_cycle = cycle(self.players)
        self.first_to_act = self.get_next_player()

    def __repr__(self):
        return_string = ""
        for player in self.players:
            return_string += str(player) + "\n"
        return return_string

    def get_player_order(self):
        """Each player rolls a dice to determine the order of play- Highest roll starts first.
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

    def get_players(self):
        return self.players

    def get_first_to_act(self):
        """Returns the Player that is first to act in a round"""
        return self.first_to_act

    def players_remaining(self):
        num_remaining = 0
        for player in self.players:
            if player.is_remaining():
                num_remaining += 1

        return num_remaining

    def get_next_player(self):
        next_player = next(self.player_cycle)
        if next_player.is_remaining():
            return next_player
        else:
            return self.get_next_player()

    def all_players_roll_dice(self):
        for player in self.players:
            player.roll()

    def reset_cycle(self):
        while next(self.player_cycle) is not self.first_to_act:
            continue

    def play_round(self):
        self.all_players_roll_dice()
        for player in self.players:
            print(player)
        bidder = self.first_to_act
        print(f"{bidder.get_name()} must make a bid!")
        bid = bidder.bid()

        # Ensure that self.player_cycle is set to the position of bidder so that responder is
        # correct player after get_next_player() called.
        self.reset_cycle()

        responder = self.get_next_player()

        # response is either instance of Bid, Call, or ExactCall
        response = faceoff(bidder, bid, responder)

        # Repeatedly have faceoffs until a Call or ExactCall response
        while isinstance(response, Bid):
            bidder, responder = responder, self.get_next_player()
            response = faceoff(bidder, response, responder)

        if isinstance(response, ExactCall):
            self.resolve_exactcall(response)
            return

        if isinstance(response, Call):
            self.resolve_call(response)
            return

        # Shouldn't ever reach here....

    def resolve_call(self, call):
        bidder = call.get_bidder()
        bid = call.get_bid()
        caller = call.get_caller()
        bid_quantity = bid.get_quantity()

        total = self.get_total(bid)

        if total >= bid_quantity:
            # bidder won & caller lost.
            caller.lose_die()

            # Was caller just eliminated from game?
            if caller.is_remaining():
                self.first_to_act = caller
            else:
                self.first_to_act = self.get_next_player()
        else:
            # caller won & bidder lost.
            bidder.lose_die()

            # Was bidder just eliminated from game?
            if bidder.is_remaining():
                self.first_to_act = bidder
            else:
                self.first_to_act = caller

    def resolve_exactcall(self, exactcall):
        bidder = exactcall.get_bidder()
        bid = exactcall.get_bid()
        caller = exactcall.get_caller()
        bid_quantity = bid.get_quantity()

        total = self.get_total(bid)

        if total == bid_quantity:
            # caller won the ExactCall
            caller.gain_die()
            self.first_to_act = bidder
        else:
            # caller lost the ExactCall
            caller.lose_die()

            # Was caller just eliminated from game?
            if caller.is_remaining():
                self.first_to_act = caller
            else:
                self.first_to_act = self.get_next_player()

    def get_all_dice_values(self):
        dice_values = []
        for player in self.players:
            dice_values += player.get_dice_values()
        return dice_values

    def get_total(self, bid):
        values = self.get_all_dice_values()
        total = values.count(1)  # 1's count as everything.
        return total if bid.is_ace_bid() else total + values.count(bid.get_value())
