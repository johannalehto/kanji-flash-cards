from learn import Learn
from review import Review

class UI:
    def __init__(self, kanjiset):
        self.kanjiset = kanjiset
        self.learn_set = Learn(kanjiset)
        self.review_set = Review(kanjiset)

    def start(self):
        print("")
        print("###########################################")
        print("###########################################")
        print("")
        print("KANJI FLASH CARDS")
        print("")

        while True:
            self.instructions()
            command = input("Give a command: ").lower()

            if command == "q":
                break
            elif command == "1":
                self.learn()
            elif command == "2":
                self.review()

    def learn(self):
        self.learn_set.display_cards()

    def review(self):
        self.review_set.review_cards()
        
    def instructions(self):
        print("-----------MAIN MENU:--------------")
        print("Press")
        print("1 - Learn a set of kanji")
        print("2 - Review a set of kanji")
        print("Q - Quit")
        print("-----------------------------------")


