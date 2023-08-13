import random
from card import Card
class Deck:
    def __init__(self):
        self.cards = []
        self.build() # när kortleken initierar byggs korten

    def build(self):
        suits = ['Spades♠️', 'Hearts❤️', 'Diamonds♦️', 'Clubs♣️']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen👸', 'King🤴']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()

        else:
            return None
