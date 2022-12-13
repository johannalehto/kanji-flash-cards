class Kanji:
    """ Class for a single Kanji
    """


    def __init__(self, character: str, english: str):
        """Class constructor to create a new Kanji entity
        Args:
            _character (str): Japanese kanji character
            _english (str): English translation
            _onyomi (tuple): Japanese readings in hiragana, katakana and romaji
            _kunyomi (tuple): Japanese readings in hiragana, katakana and romaji
        """
        # self._id = 1
        self._character = character
        self._english = english
        # self._onyomi = onyomi
        # self._kunyomi = kunyomi

    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, char: str):
        self._character = char

    @property
    def english(self):
        return self._english

    @english.setter
    def english(self, eng: str):
        self._english = eng

    # @property
    # def onyomi(self):
    #     return self._onyomi

    # @onyomi.setter
    # def onyomi(self, ony: tuple):
    #     self._onyomi = ony

    # @property
    # def kunyomi(self):
    #     return self._kunyomi

    # @onyomi.setter
    # def kunyomi(self, kun: tuple):
    #     self._kunyomi = kun
