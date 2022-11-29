from ui.io import Io
from entities.card import Card
from entities.pile import Pile

class LearnView:
    def __init__(self, pile: Pile):
        self.pile = pile
        self.io = Io()

    def display_cards(self):
   #     self.print_title()

        for card in self.pile:
            self.io.write(str(card))
            command = self.io.read("")
            if command == "":
                self.io.write(f'MEANING: {card.meaning()}')
            command = self.io.read("")
            if command == "":
                continue
        self.print_ending()

    @classmethod
    def print_title(cls):
        print("")
        print("###########################################")
        print("")
        print("Showing a set of 5 kanji")
        print("Press enter to see the meaning and move on to a next card")

    @classmethod
    def print_ending(cls):
        print("-------------------------------------")
        print("End of the set")


