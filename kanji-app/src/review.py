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
