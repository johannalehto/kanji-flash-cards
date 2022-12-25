from tkinter import Tk
from ui.gui import GUI

BACKGROUND_COLOR = "#fff"

def main():
    window = Tk()
    window.title("Kanji Flashcards App")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    word_file = "./src/data/default.csv"
    kanjiapp = GUI(window, word_file)
    kanjiapp.start()

    window.mainloop()


if __name__ == "__main__":
    main()
