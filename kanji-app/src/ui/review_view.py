from ui.io import Io
from entities.pile import Pile
from entities.session import Session
from services.kanji_service import KanjiService

class ReviewView:
    def __init__(self):
        self.io = Io()
        self.service = KanjiService()
        self.pile = Pile()
        self.cards_per_round = 5
        self.session = Session()

    def set_pile(self, pile):
        self.pile = pile

    def display_review_pile(self, pile):
        self.set_pile(pile)
        self.set_cards_per_round()
        self.print_title()

        for card in self.pile:
            self.io.write(str(card))
            user_answer = self.io.read("MEANING: ").lower()

            if self.service.check_meaning(user_answer, card):
                self.session.add_point()
                self.io.write("")
                self.io.write('Correct!')
            else:
                self.io.write("")
                self.io.write(f'Wrong. The right answer is:  {card.meaning()}')

            command = self.io.read("")
            if command == "":
                continue

        self.print_ending()
        self.show_points()
        self.return_to_main_menu()



    def show_points(self):
        self.io.write(f'You got {self.session.session_points()} / {len(self.pile)} correct')

    def return_to_main_menu(self):
        self.io.write("")
        command = self.io.read("> Press ENTER to return to the main menu")
        self.io.write("")
        if command == "":
            return

    def set_cards_per_round(self):
        self.io.write("")
        self.io.write(f"Your current card set has {len(self.pile)} cards.")
        # while True:
        #     new_cards_per_round = self.io.read("How many cards do you want to learn: ")
        #     if int(new_cards_per_round) < len(self.pile):
        #         self.io.write("You don't have enough cards. Give a smaller amount.")
        #     break
        # self.cards_per_round = int(new_cards_per_round)
        self.cards_per_round = len(self.pile)


    def print_title(self):
        self.io.write(f"Showing a set of {self.cards_per_round} kanji")
        self.io.write("")
        self.io.write("INSTRUCTIONS:")
        self.io.write("Write the meaning in English and press enter to move on to a next card")
        self.io.write("")
        self.io.write("")
        command = self.io.read("> Press ENTER to start")
        self.io.write("")
        if command == "":
            return

    def print_ending(self):
        self.io.write("-------------------------------------")
        self.io.write("End of the set")

