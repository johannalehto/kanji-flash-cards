from ui.io import Io
from ui.learn_view import LearnView
from ui.review_view import ReviewView



class UI:
    def __init__(self, kanjiset):
        self.io = Io()
        self.kanjiset = kanjiset

        self.learn_set = Learn(kanjiset)
        self.review_set = Review(kanjiset)

    def start(self):
        self.title()
        while True:
            self.instructions()
            command = self.io.read("Give a command: ")
            if command == "q":
                break
            if command == "1":
                self.display_learn()
            if command == "2":
                self.display_review()

    def display_learn(self):

        self.learn_set.display_cards()

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
