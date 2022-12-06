from ui.io import Io
from entities.pile import Pile

class LearnView:
    def __init__(self):
        self.io = Io()
        self.pile = Pile()
        self.cards_per_round = 5

    def display_learn_pile(self, pile):
        self.set_pile(pile)
        self.set_cards_per_round()
        self.print_title()

        for card in self.pile:
            self.io.write(str(card))
            command = self.io.read("")
            if command == "":
                self.io.write(f'MEANING: {card.meaning()}')
            command = self.io.read("")
            if command == "":
                continue
        self.print_ending()


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
        self.io.write(f"Showing a set of {self.cards_per_round} kanji")
        self.io.write("")
        self.io.write("INSTRUCTIONS:")
        self.io.write("Press enter to see the meaning and move on to a next card")
        self.io.write("")
        self.io.write("")
        command = self.io.read("> Press ENTER to start")
        self.io.write("")
        if command == "":
            return

    def print_ending(self):
        self.io.write("-------------------------------------")
        self.io.write("End of the set")


