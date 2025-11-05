import Card as card
import random
class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in card.suits:
            for rank in card.ranks:
                created_card = card.Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop()

    def __str__(self):
        deck_comp = ''
        for card in self.all_cards:
            deck_comp += '\n' + card.__str__()
        return deck_comp

