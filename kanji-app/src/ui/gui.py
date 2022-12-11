from tkinter import Tk, ttk, Canvas

BACKGROUND_COLOR = "#fff"

class GUI:
    def __init__(self, root):
        self._root = root

    def start(self):
        label = ttk.Label(master=self._root, text="Hello world!")

        label.pack()

window = Tk()
window.title("Kanji Flashcards App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



ui = GUI(window)
ui.start()

window.mainloop()