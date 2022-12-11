from tkinter import *
from services.kanji_service import KanjiService

BACKGROUND_COLOR = "#fff"

class ReviewGUI:
    """Display for reviewing the cards."""

    def __init__(self, root, handle_return):
        """Class constructor. Creates a class for the review.

        Args:
            root:
                TKinter-element where the Review UI is initialized.
            handle_return:
                Value called after the end of the set for returning to main menu.
        """

        self._root = root
        self._handle_return = handle_return
        self._service = KanjiService()
       # self._pile = self._service.get_new_pile()
        self._canvas = None
        self._card_meaning_entry = None
        self._answer = None

        self._initialize()

    def pack(self):
        """"Displays the view"""
        self._canvas.pack()

    def destroy(self):
        """"Destroys the view"""
        self._canvas.destroy()

    def _return_handler(self):
        self._handle_return()

    def _handle_answer(self):
        self._answer = self._card_meaning_entry.get()


    def _initialize(self):
        self._canvas = Canvas(self._root, width=800, height=400)
        self._canvas.pack()

        self._initialize_card()
        self._initialize_entry_form()

        self._canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self._canvas.grid(row=0, column=0, columnspan=2)

    def _initialize_card(self):
        card_character = self._canvas.create_text(
            400, 150, 
            text="漢字", 
            font=("Arial", 80, "bold"))

    
    def _initialize_entry_form(self):
        card_meaning_title = self._canvas.create_text(
            400, 250, 
            text="meaning:", 
            font=("Arial", 24))

        card_meaning_entry = Entry(
            master=self._root, 
            font=("Arial", 24), 
            width=34, 
            fg="#000")

        entry_window = self._canvas.create_window(
            400, 300, 
            window=card_meaning_entry)

