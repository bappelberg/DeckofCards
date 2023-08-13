from deck import Deck


class Game:
    def __init__(self):
        self.deck = Deck()

    def play(self):
        self.deck.shuffle()

        while True:
            if len(self.deck.cards) == 0:
                print('No more cards to draw')
                break

            user_input = input("Press Enter to draw a card (q to quit): ")

            if user_input.lower() == 'q':
                break

            card = self.deck.draw_card()
            print(f'\tYou drew {card.value} of {card.suit}. Remaining cards to draw: {len(self.deck.cards)}')
