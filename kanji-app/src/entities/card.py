from entities.kanji import Kanji


class Card:
    """Class for a new Card which receives a kanji"""

    def __init__(self, kanji):
        """Class constructor to create a new Card entity
        Args:
            _kanji (Kanji()): Kanji object
            _correct_level_1 (Bool): Store in which level the user has card
            _correct_level_2 (Bool): Store in which level the user has card
            _correct_level_2 (Bool): Store in which level the user has card

        """
        self.kanji = Kanji(kanji[0], kanji[1])
        # self._correct_level_1 = False
        # self._correct_level_2 = False
        # self._correct_level_3 = False


    def meaning(self):
        """Returns the English meaning"""
        return self.kanji.english

    def character(self):
        """Returns the Japanese character"""
        return self.kanji.character

    def __str__(self):
        return f'{40 * "-"} \n KANJI: {self.kanji.character} \n {40 * "-"}'
