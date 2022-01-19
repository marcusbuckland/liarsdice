from call import Call


class ExactCall(Call):
    """
    Represents an ExactCall action in the game. A Player makes an ExactCall action when they posit that the quantity
     of the dice rolled by all players of the current Bid value is exactly equal to the quanitity of the current Bid.
     An ExactCall action ends a bidding round.
    """

    def __init__(self, bidder, bid, caller):
        super().__init__(bidder, bid, caller)
