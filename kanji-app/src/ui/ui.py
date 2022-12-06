from ui.io import Io
from ui.learn_view import LearnView
from ui.review_view import ReviewView

from services.kanji_service import KanjiService


class UI:
    def __init__(self):
        self.io = Io()
        self.list = None
        self.service = KanjiService()
        self.learn = LearnView()
        self.review = ReviewView()
        self.new_pile = []


    def run(self):
   
        self.title_main()
        self.title_create_cardset()
        self.create_new_pile()

        while True:
            self.instructions()
            command = self.io.read("Give a command: ")
            if command == "q":
                break
            if command == "1":
                self.learn.display_learn_pile(self.new_pile)
            if command == "2":
                self.review.display_review_pile(self.new_pile)


    def enter_file(self):
       # words_file = input("Add .csv -file to create a card set or press ENTER to use a default set:")
        words_file = self.io.read("> Press ENTER to use a default card set \n")
        if words_file == "":
            words_file = "./src/data/default.csv"
        return words_file

    def create_new_pile(self):
        word_file = self.enter_file()
        self.new_pile = self.service.create_cardset_from_file(word_file)
        self.io.write("")
        self.io.write("")
        self.io.write("* New card set created! *")

    def title_main(self):
        self.io.write("")
        self.io.write("")
        self.io.write(f"{40 * '-'}")
        self.io.write("")
        self.io.write("KANJI FLASH CARDS")
        self.io.write("")

    def title_create_cardset(self):
        self.io.write("")
        self.io.write("--Create a new card set--")
        self.io.write("")

    def instructions(self):
        self.io.write("")
        self.io.write("")
        self.io.write("-----------MAIN MENU:--------------")
        self.io.write("Press")
        self.io.write("1 - Learn a set of kanji")
        self.io.write("2 - Review a set of kanji")
        self.io.write("Q - Quit")
        self.io.write("-----------------------------------")
