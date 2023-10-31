from deck import Deck
from pprint import pprint
from hand import Hand
from dealer_hand import Dealer_Hand
from player_hand import Player_Hand

deck = Deck(6)
dealer_hand = Dealer_Hand()
player_hand = Player_Hand("Player_One")


def deal_start(dealer_hand: Hand, player_hand: Hand, deck: Deck):
    dealer_hand.add_card_to_hand(deck.draw_card())
    player_hand.add_card_to_hand(deck.draw_card())
    dealer_hand.add_card_to_hand(deck.draw_card())
    player_hand.add_card_to_hand(deck.draw_card())


deal_start(dealer_hand, player_hand, deck)

dealer_hand.say_up_card()
player_hand.say_cards()
player_hand.calculate_totals()
player_hand.say_values()
