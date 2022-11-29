from entities.kanji import Kanji

class Card: 
    def __init__(self, kanji):
        self._kanji = Kanji()
        # self._correct_level_1 = False
        # self._correct_level_2 = False
        # self._correct_level_3 = False

    def meaning(self):
        return self._kanji.english

    def __str__(self):
        print(f'{40 * "-"} \n KANJI: {self._kanji._character} \n {40 * "-"}')
