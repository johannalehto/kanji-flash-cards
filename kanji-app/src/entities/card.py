from entities.kanji import Kanji


class Card:
    """Class for a new Card which receives a kanji"""

    def __init__(self, character: str, meaning: str):
        """Class constructor to create a new Card entity
        Args:
            _kanji (Kanji()): Kanji object
        """
        self._kanji = Kanji(character, meaning)


    def meaning(self):
        """Returns the English meaning"""
        return self._kanji.english

    def character(self):
        """Returns the Japanese character"""
        return self._kanji.character

