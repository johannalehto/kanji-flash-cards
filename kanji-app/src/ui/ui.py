from ui.io import Io
from ui.learn_view import LearnView
from ui.review_view import ReviewView

from services.kanji_service import KanjiService
from entities.pile import Pile



class UI:
    def __init__(self, kanjiset):
        self.io = Io()
        self.list = kanjiset
        self.service = KanjiService()
        self.learn = LearnView
        self.new_pile = None


    def run(self):
        self.new_pile = self.service.create_pile_from_list(self.list)

        self.title()
        while True:
            self.instructions()
            command = self.io.read("Give a command: ")
            if command == "q":
                break
            if command == "1":
                self.display_learn()
            if command == "2":
                self.io.write("Under maintenance")
                # self.display_review()


    def display_learn(self):
        self.learn.display_cards(self.new_pile)


    def display_review(self):
        self.review_set.review_cards()


    def title(self):
        self.io.write("")
        self.io.write("")
        self.io.write(f"{40 * '-'}")
        self.io.write("")
        self.io.write("KANJI FLASH CARDS")
        self.io.write("")


    def instructions(self):
        self.io.write("-----------MAIN MENU:--------------")
        self.io.write("Press")
        self.io.write("1 - Learn a set of kanji")
        self.io.write("2 - Review a set of kanji")
        self.io.write("Q - Quit")
        self.io.write("-----------------------------------")
