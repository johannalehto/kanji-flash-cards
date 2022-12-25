class Kanji:
    """ Class for a single Kanji"""

    def __init__(self, character: str, english: str):
        """Class constructor to create a new Kanji entity
        Args:
            _character (str): Japanese kanji character
            _english (str): English translation
        """
        self._character = character
        self._english = english

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

