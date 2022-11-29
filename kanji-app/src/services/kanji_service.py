from entities.kanji import Kanji
from entities.card import Card
from entities.pile import Pile
import json


class KanjiService:
    """ Application logic """

    def __init__(self):
        self.set = []
        self.new_pile = Pile()

    def create_pile_from_list(self, kanjilist: list):
        self.create_set_from_list(kanjilist)
        self.create_pile_from_set()
        return self.new_pile

        
    def create_set_from_list(self, kanjilist):
        with open(kanjilist) as listfile: 
            dir = json.loads(listfile.read())
        for k in dir: 
            self.set.append(Kanji(k["character"], k["english"], k["onyomi"], k["kunyomi"])) 

    def create_pile_from_set(self):
        for item in self.set: 
            self.new_pile.add_kanji(item)



