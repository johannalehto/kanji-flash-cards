import csv
from entities.pile import Pile


class KanjiService:
    """ Application logic """

    def __init__(self):
        self.new_pile = Pile()

    def create_cardset_from_file(self, word_file: str):
        with open(word_file) as words:
            all_words = csv.reader(words, delimiter=";")
            for word in all_words:
                self.new_pile.add_kanji(word)
        return self.new_pile.cards()


    def check_meaning(self, user_answer: str, card):
        if user_answer == card.meaning():
            return True
        return False


