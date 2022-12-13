
from entities.card import Card


class Pile:
    """Class for a new Pile which stores a set of cards"""

    def __init__(self):
        """Class constructor to create a new pile object for set of cards
        Args:
            _cards (list): List to store several Card objects
        """
        self._cards = []

    def add_kanji(self, new_kanji):
        """Adds new card object to the list"""
        self._cards.append(Card(new_kanji))

    def cards(self):
        return self._cards
