class Call:
    """
    Represents when a player calls a bid- ending that bidding round and starting the comparisons.
    """

    def __init__(self, bidder, bid, caller):
        self.bidder = bidder
        self.bid = bid
        self.caller = caller

    def get_bidder(self):
        return self.bidder

    def get_bid(self):
        return self.bid

    def get_caller(self):
        return self.caller
