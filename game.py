from player import Player
from itertools import cycle

from bid import Bid
from player import Player
from call import Call
from exactcall import ExactCall

class Game():
    """ Represents an actual instance of the game Liar's Dice (Dudo)."""
    def __init__(self):
        self.players = self.generate_players()
        self.player_cycle = cycle(self.players)
        self.first_to_act = self.get_next_player()

    def __repr__(self):
        return_string = ""
        for player in self.players:
            return_string += str(player) + "\n"
        return return_string
        
    def generate_players(self):
        num_players = int(input("How many players are playing?"))
        players = []
        
        # Create the Player objects and store them inside players list
        for i in range(num_players):
            name = input("Player's name?")
            players.append(Player(name))
        return players

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
                num_remaining+=1
            
        return num_remaining

    def get_next_player(self):
        next_player = next(self.player_cycle)
        if next_player.is_remaining() : 
            return next_player
        else :
            return self.get_next_player()

    def all_players_roll_dice(self):
        for player in self.players:
            player.roll()

    def play_round(self) : 
        print("Playing Round!")
        self.all_players_roll_dice()
        bidder = self.first_to_act
        print(f"{bidder.get_name()} must make a bid!")
        bid = bidder.bid(previous_bid=None)
        responder = self.get_next_player()
        response = self.faceoff(bidder, bid, responder)

        # Repeatedly have faceoffs until a Call or ExactCall response
        while isinstance(response, Bid):
            bidder, responder = responder, self.get_next_player()
            response = self.faceoff(bidder, response, responder)

        if isinstance(response, Call):
            call = response
            self.check_results(bid, call)
            pass

        if isinstance(response, ExactCall):
            exact_call = response
            self.check_results(bid, exact_call)
            pass

        # Shouldn't ever reach here....

    def faceoff(self, bidder, bid, responder):
        print(f"{bidder.get_name()} has made a bid of: {bid}.")
        print(f"{responder.get_name()} is responding to {bidder.get_name()}'s bid...")

        response = self.get_bid_response()

        # Bid response
        if response == "Bid":
            response_bid = responder.bid(previous_bid=bid)
            print(f"{responder.get_name()} responds with a bid of: {response_bid}")
            return response_bid

        # Call response
        if response == "Call" : return


        # ExactCall response
        if response == "ExactCall" : return

    def get_bid_response(self):
        while True:
            response = input("Response: ")
            if response in ["Bid", "Call", "ExactCall"]:
                return response
            else :
                print("Invalid response!")
                continue