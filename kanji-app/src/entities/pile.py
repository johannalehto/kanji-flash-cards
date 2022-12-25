
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
        character = new_kanji[0]
        meaning = new_kanji[1]
        self._cards.append(Card(character, meaning))

    def cards(self):
        return self._cards
