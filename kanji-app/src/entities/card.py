from entities.kanji import Kanji


class Card:
    """Class for a new Card which receives a kanji"""

    def __init__(self, kanji):
        """Class constructor to create a new Card entity
        Args:
            _kanji (Kanji()): Kanji object
        """
        self.kanji = Kanji(kanji[0], kanji[1])


    def meaning(self):
        """Returns the English meaning"""
        return self.kanji.english

    def character(self):
        """Returns the Japanese character"""
        return self.kanji.character

