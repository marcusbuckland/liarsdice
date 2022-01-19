class Call:
    """
    Represents a Call action in the game. A Player makes a Call action when they posit the current
     Bid is unlikely to succeed. A Call action ends a bidding round.
    """

    def __init__(self, bidder, bid, caller):
        self.bidder = bidder
        self.bid = bid
        self.caller = caller

    def get_bidder(self):
        """The Player that made the Bid which has been called."""
        return self.bidder

    def get_bid(self):
        """The Bid that has been called."""
        return self.bid

    def get_caller(self):
        """The Player that has called the bid."""
        return self.caller
