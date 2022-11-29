from entities.card import Card

class LearnView:
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
