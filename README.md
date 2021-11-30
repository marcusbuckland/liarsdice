# liarsdice

# To do list

* Ensure logic of lt and gt for bids is correct (Write tests????)
* Set up the Game class which is going to be an instance of an actual game of Liar's dice
* Test equals case for gt and lt

# Game class

# Fields ? 
*  players field which stores the Player objects (list of Player() objects)
*  players_cycle which cycles through the players remaining
*  game_finished - boolean True/False

*  write the method for playing a round.

* rounds are made of of a series of bids which go higher and higher.
* round can perhaps be broken down into smaller actions, which is basically first a bid and then second a response.
* a response can be a higher bid, a call, or an exact call.
* possibly I can make a class such as "Action" which is a super class of Bid, Call, and ExactCall?
* then logic is response = player.get_response()
* if response isinstance(Bid) -> then re-do.
* elif response isinstance(Call) -> initiate call process and end the round.
* else (response must be ExactCall) -> initiate ExactCall process and end the round.

# Things to keep in mind-

* Cannot simply just say "get next player" all the time because the player to begin a round will change depending on if a call was successful or not.
* Should make a field in the __init__ method called "first_to_act" and then update this player depending on what happened at the end of the round.
* this means need to keep a track of not only the Bid and if it was successful or not, but the player that made the bid.
* Possible a bid object needs to have an "owner"- ie the person that made the bid?

* is_finished()


# Bid class

* Create a method called value() which would simplify the logic in the __lt__ and __gt__ methods.


* Flow of the game is something like....

# Set-up / Initialisation:

* Set up all players, each starts with 6 die objects
* Randomly select a player to start

# Start of game :
* Have a round
* Have the loser of the round lose a die object
* Have the winner of the round gain a die (if relevant)
* Set up the first_to_act player depending on what happened in the round.


# Game continues : 
* Have another round... etc (repeat above)
* Continue having rounds until the game is finished. e.g.
* while game.not_finished() :
*     play_round()

# Game finished (just after the while loop logic)
* print the winners name???



# Can expand the game by changing how the ordering of players is deciding, by rolling dice (see the wikipedia page for rules)

# Make it so bid values can only be between 1 and 6
# Make it so bid quantities can only be between 1 and num_dice_remaining

# Should ExactCall class inherit from Call?