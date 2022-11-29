
class ReviewView:
    def __init__(self, kanjiset):
        self.kanjiset = kanjiset
        self.session_points = 0

    def check_meaning(self, user_answer, card_answer):
        if user_answer == card_answer:
            self.session_points += 1
            return 'Correct!'
        return f'Wrong. The right answer is:  {card_answer}'

    def check_cards(self):
        for card in self.kanjiset:
            print("-----------------------------------")
            print("")
            print(f'KANJI: {card["kanji"]}')
            user_answer = input("MEANING: ").lower()
            print(self.check_meaning(user_answer, card["english"]))

            command = input("")
            if command == "":
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

        self.check_cards()

        print("-----------------------------------")
        print("")
        print("End of the set")

        self.show_points()

        self.return_to_main_menu()
