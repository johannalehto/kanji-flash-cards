from tkinter import *

BACKGROUND_COLOR = "#fff"

class GUI:
    def __init__(self, root):
        self._root = root

    def start(self):        
        canvas = Canvas(self._root, width=800, height=400)
        canvas.pack()
        card_character = canvas.create_text(400, 150, text="漢字", font=("Arial", 80, "bold"))
        card_meaning_title = canvas.create_text(400, 250, text="meaning:", font=("Arial", 24))

        card_meaning_entry = Entry(master=self._root, font=("Arial", 24), width=34, fg="#000")
        entry_window = canvas.create_window(400, 300, window=card_meaning_entry)

        canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        canvas.grid(row=0, column=0, columnspan=2)


window = Tk()
window.title("Kanji Flashcards App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


ui = GUI(window)
ui.start()

window.mainloop()