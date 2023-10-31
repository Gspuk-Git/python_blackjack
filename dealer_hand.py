from hand import Hand


class Dealer_Hand(Hand):
    owner = "Dealer"
    cards = []
    totals = []

    def say_up_card(self):
        suit = self.cards[0]["suit"]
        name = self.cards[0]["name"]
        values = self.cards[0]["values"]
        print("%s has:" % (self.owner))
        print("  %s of %s." % (name, suit))
        Hand.say_values(values)
