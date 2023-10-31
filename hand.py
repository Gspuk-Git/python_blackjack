class Hand:
    def calculate_totals(self):
        totals = []
        total
        for card in self.cards:
            total = 0
            for value in card["values"]:
                total += value

            totals.append(total)

        self.totals = totals

    def add_card_to_hand(self, card):
        self.cards.append(card)

    def say_cards(self):
        print("%s has:" % (self.owner))
        for card in self.cards:
            print("  %s of %s." % (card["name"], card["suit"]))

    def say_values(values):
        values_string = "total: " + str(values[0])

        print(values)

        if len(values) > 1:
            for value in values:
                values_string + " or " + str(value)

        values_string + "."

        print(values_string)
