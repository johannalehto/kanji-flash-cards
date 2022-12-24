import csv
from entities.pile import Pile


class KanjiService:
    """ Application logic """

    def __init__(self):
        """Class constructor. Creates a class for the application logic.

        Args:
            _new_pile:
                Stores the set of cards
        """
        self.new_pile = Pile()

    def create_cardset_from_file(self, word_file: str):
        """ Creates a new set of cards, receives a csv-file"""
        with open(word_file) as words:
            all_words = csv.reader(words, delimiter=";")
            for word in all_words:
                self.new_pile.add_kanji(word)
        return self.new_pile.cards()

    def check_meaning(self, user_answer: str, card):
        """ Compares the users answer to the meaning stored in Card-object"""
        if user_answer == card.meaning():
            return True
        return False
