from entities.kanji import Kanji


class Card:
    def __init__(self, kanji: Kanji):
        self.kanji = kanji
        # self._correct_level_1 = False
        # self._correct_level_2 = False
        # self._correct_level_3 = False

    def meaning(self):
        return self.kanji.english

    def character(self):
        return self.kanji.character

    def __str__(self):
        return f'{40 * "-"} \n KANJI: {self.kanji.character} \n {40 * "-"}'
