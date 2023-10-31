from hand import Hand


class Player_Hand(Hand):
    cards = []
    totals = []

    def __init__(self, owner: str):
        self.owner = owner

    def say_values(self):
        Hand.say_values(self.totals)
