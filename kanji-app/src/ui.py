


class Learn:
    def __init__(self, kanjiset):
        self.kanjiset = kanjiset

    def display_cards(self):
        print("")
        print("###########################################")
        print("")
        print("Showing a set of 5 kanji")
        print("Press enter to see the meaning and move on to a next card")
        for card in self.kanjiset:
            print("-------------------------------------")
            print("")
            print(f'KANJI: {card["kanji"]}')
            command = input("")
            if command == "":
                print(f'MEANING: {card["english"]}')
            command = input("")
            if command == "":
                continue
        print("-------------------------------------")
        print("End of the set")


class Review:
    def __init__(self, kanjiset):
        self.kanjiset = kanjiset


    def review_cards(self):
        print("")
        print("###########################################")
        print("")
        print("Showing a set of 5 kanji")
        print("Write the meaning in English and press enter to move on to a next card")


        for card in self.kanjiset:
            print("-------------------------------------")
            print("")
            print(f'KANJI: {card["kanji"]}')
            answer = input("MEANING: ")
            if answer == card["english"]:
                print(f'Correct!')
            else:
                print(f'Wrong. The right answer is:: {card["english"]}')
            command = input("")
            if command== "":
                continue
        print("-------------------------------------")
        print("End of the set")




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


