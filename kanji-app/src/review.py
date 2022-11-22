class Review:
    def __init__(self, kanjiset):
        self.kanjiset = kanjiset
        self.session_points = 0


    def place_cards(self):
        for card in self.kanjiset:
            print("-----------------------------------")
            print("")
            print(f'KANJI: {card["kanji"]}')
            answer = input("MEANING: ")
            if answer == card["english"]:
                print(f'Correct!')
                self.session_points += 1
            else:
                print(f'Wrong. The right answer is:  {card["english"]}')
            command = input("")
            if command== "":
                continue
    
    def show_points(self):
        print(f'You got {self.session_points} / {len(self.kanjiset)} correct')

    def return_to_main_menu(self):
        print("")
        command = input("Press enter to return to the main menu")
        print("")
        if command == "":
            return


    def review_cards(self):
        print("")
        print("###########################################")
        print("")
        print("Showing a set of 5 kanji")
        print("Write the meaning in English and press enter to move on to a next card")

        self.place_cards()

        print("-----------------------------------")
        print("")
        print("End of the set")

        self.show_points()

        self.return_to_main_menu()


