import card_constants
import random


class Deck:
    cards = []

    def __init__(self, num_decks: int):
        i = 0
        while i < num_decks:
            for suit in card_constants.suits:
                for card_name_values in card_constants.card_names_values:
                    self.cards.append(
                        {
                            "name": card_name_values["name"],
                            "suit": suit,
                            "values": card_name_values["values"],
                        }
                    )
            i += 1

        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

    def cards_left(self):
        return self.cards.count()
