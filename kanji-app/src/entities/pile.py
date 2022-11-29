from entities.kanji import Kanji
from entities.card import Card


class Pile:
    def __init__(self):
        self._cards = []

    def add_kanji(self, new_kanji: Kanji):
        self._cards.append(Card(new_kanji))

    def cards(self):
        return self._cards
