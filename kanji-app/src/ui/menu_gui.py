from tkinter import *
from services.kanji_service import KanjiService

BACKGROUND_COLOR = "#fff"
word_file = "./src/data/default.csv"

class MenuGUI:
    """Display for the main menu of the app."""
    def __init__(self, root):
        """Class constructor. Creates a class for the review.

        Args:
            _root:
                TKinter-element where the Main menu UI is initialized.
        """
        self._root = root
        self._canvas = None

        self._display_menu()

    def _initialize(self):
        """"Initializes the card round view"""
        self._canvas = Canvas(self._root, width=800, height=526)
        self._canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self._canvas.grid(row=0, column=0, columnspan=2)

    
    def _display_menu():
        pass


    def pack(self):
        """"Displays the view"""
        self._canvas.pack()

    def destroy(self):
        """"Destroys the view"""
        self._canvas.delete('all')



