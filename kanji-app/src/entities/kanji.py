class Kanji:
    def __init__(self):
        self._id = 1
        self._character = "山"
        self._english = "mountain"
        self._onyomi = ("さん", "サン", "san")
        self._kunyomi = ("やま", "ヤマ", "yama")

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

    @property
    def onyomi(self):
        return self._onyomi

    @onyomi.setter
    def onyomi(self, on: tuple):
        self._onyomi = on

    @property
    def kunyomi(self):
        return self._kunyomi

    @onyomi.setter
    def kunyomi(self, kun: tuple):
        self._kunyomi = kun

    

