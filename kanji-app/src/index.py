from tkinter import Tk
#from ui.ui import UI
from ui.gui import GUI

BACKGROUND_COLOR = "#fff"

def main():
    window = Tk()
    window.title("Kanji Flashcards App")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    kanjiapp = GUI(window)
    kanjiapp.start()

    window.mainloop()

# def main():
#     kanjiapp = GUI()
#     kanjiapp.run()


if __name__ == "__main__":
    main()
