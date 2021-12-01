from player import Player
from itertools import cycle
from bid import Bid
from player import Player
from call import Call
from exactcall import ExactCall


def generate_players():
    num_players = int(input("How many players are playing?"))
    players = []

    # Create the Player objects and store them inside players list
    for i in range(num_players):
        name = input("Player's name?")
        players.append(Player(name))
    return players


def get_bid_response():
    while True:
        response_string = input("Response: ")
        if response_string in ["Bid", "Call", "ExactCall"]:
            return response_string
        else:
            print("Invalid response!")
            print("Choose one of 'Bid', 'Call', or 'ExactCall'")
            continue


class Game:
    """ Represents an actual instance of the game Liar's Dice (Dudo)."""

    def __init__(self):
        self.players = generate_players()
        self.player_cycle = cycle(self.players)
        self.first_to_act = self.get_next_player()  # Fine for now- but we can expand this further (roll for start)

    def __repr__(self):
        return_string = ""
        for player in self.players:
            return_string += str(player) + "\n"
        return return_string

    def is_finished(self):
        return self.players_remaining() <= 1

    def get_players(self):
        return self.players

    def get_first_to_act(self):
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

        print("Playing Round!")
        self.all_players_roll_dice()
        print(self.players)
        bidder = self.first_to_act
        print(f"{bidder.get_name()} must make a bid!")
        bid = bidder.bid()

        # Ensure that self.player_cycle is set to the position of bidder so that responder is
        # correct player after get_next_player() called.
        self.reset_cycle()

        responder = self.get_next_player()

        # response is either instance of Bid, Call, or ExactCall
        response = self.faceoff(bidder, bid, responder)

        # Repeatedly have faceoffs until a Call or ExactCall response
        while isinstance(response, Bid):
            bidder, responder = responder, self.get_next_player()
            response = self.faceoff(bidder, response, responder)

        if isinstance(response, Call):
            # response was a call. Need to
            # 1. Check if the bid was won or not.
            # 2. Make the loser of the faceoff (either bidder of caller) lose a die.
            # 3. set self.first_to_act = loser.
            # 4. exit this method.
            caller = responder
            self.resolve_call(bidder, bid, caller)
            pass

        if isinstance(response, ExactCall):
            exactcall = response
            self.reslove_exactcall(bid, exactcall)
            pass

        # Shouldn't ever reach here....

    def faceoff(self, bidder, bid, responder):
        print(f"{bidder.get_name()} has made a bid of: {bid}.")
        print(f"{responder.get_name()} is responding to {bidder.get_name()}'s bid...")

        response_string = get_bid_response()

        # Bid response
        if response_string == "Bid":
            response_bid = responder.bid(previous_bid=bid)
            print(f"{responder.get_name()} responds with a bid of: {response_bid}")
            return response_bid

        # Call response
        if response_string == "Call":
            return Call(bidder=bidder, bid=bid, caller=responder)

        # ExactCall response
        if response_string == "ExactCall":
            return ExactCall(bidder=bidder, bid=bid, caller=responder)

    def resolve_call(self, call):
        bidder = call.get_bidder()
        bid = call.get_bid()
        caller = call.get_caller()
        bid_quantity = bid.get_quantity()

        total = self.get_total()

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

    def reslove_exactcall(self, exactcall):
        bidder = exactcall.get_bidder()
        bid = exactcall.get_bid()
        caller = exactcall.get_caller()
        bid_quantity = bid.get_quantity()

        total = self.get_total()

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
        if bid.not_ace_bid():
            total += values.count(bid.get_value())
        return total
