from call import Call


class ExactCall(Call):
    """Represents when a player makes an ExactCall response- a special type of Call"""

    def __init__(self, bidder, bid, caller):
        super().__init__(bidder, bid, caller)
