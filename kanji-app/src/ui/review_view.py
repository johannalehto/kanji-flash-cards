from ui.io import Io
from entities.card import Card
from entities.pile import Pile

class ReviewView:
    def __init__(self):
        self.io = Io()
        self.pile = Pile()
        self.cards_per_round = 5
        self.session_points = 0

    
    def review_cards(self, pile):
        self.set_pile(pile)
        self.set_cards_per_round()
        self.print_title()

        for card in self.pile:
            self.io.write(str(card))
            user_answer = self.io.read("MEANING: ").lower()
            self.io.write(self.check_meaning(user_answer, card.meaning()))
            command = self.io.read("")
            if command == "":
                continue

        self.print_ending()
        self.show_points()
        self.return_to_main_menu()


    def check_meaning(self, user_answer, card_answer):
        if user_answer == card_answer:
            self.session_points += 1
            return 'Correct!'
        return f'Wrong. The right answer is:  {card_answer}'


    def show_points(self):
        self.io.write(f'You got {self.session_points} / {len(self.pile)} correct')

    def return_to_main_menu(self):
        self.io.write("")
        command = self.io.read("Press enter to return to the main menu")
        self.io.write("")
        if command == "":
            return

    def set_pile(self, pile):
        self.pile = pile

    def set_cards_per_round(self):
        self.io.write(f"Your current card set has {len(self.pile)} cards.")
        # while True:
        #     new_cards_per_round = self.io.read("How many cards do you want to learn: ")
        #     if int(new_cards_per_round) < len(self.pile):
        #         self.io.write("You don't have enough cards. Give a smaller amount.")
        #     break
        # self.cards_per_round = int(new_cards_per_round)
        self.cards_per_round = len(self.pile)


    def print_title(self):
        self.io.write("")
        self.io.write(f"Showing a set of {self.cards_per_round} kanji")
        self.io.write("Write the meaning in English and press enter to move on to a next card")

    def print_ending(self):
        self.io.write("-------------------------------------")
        self.io.write("End of the set")

