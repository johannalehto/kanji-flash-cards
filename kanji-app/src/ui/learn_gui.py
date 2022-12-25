from tkinter import *
from services.ui_service import UIService
from services.kanji_service import KanjiService
import random

BACKGROUND_COLOR = "#fff"
word_file = "./src/data/default.csv"

class LearnGUI:
    """Display for reviewing the cards."""

    def __init__(self, root, handle_return):
        """Class constructor. Creates a class for the review.

        Args:
            _root:
                TKinter-element where the Review UI is initialized.
            _handle_return:
                Value called after the end of the set for returning to main menu.
            _service:
                For accessing methods from KanjiService-object.
            _pile:
                Receives a new set of cards.
            _canvas:
                Creates structure for the visual elements.

            _character:
                Holds character in display.

            _card:
                Holds current card in display.
            


        """

        self._root = root
        self._ui_service = UIService()
        self._service = KanjiService()
        self._pile = self._service.create_cardset_from_file(word_file)
        self._session_set = self._create_session_set(amount=5)
        self._bg_color = self._ui_service.bg_color
        self._canvas = self._ui_service.initialize_canvas(self._root)
        self._handle_return = handle_return
        self._character = None
        self._card_nr = 0
        self._card = None

        self._run_cards()

    def pack(self):
        """"Displays the view"""
        self._canvas.pack()

    def destroy(self):
        """"Destroys the view"""
        self._canvas.delete('all')

    def _return_handler(self):
        """"Responsible for returning to the menu view"""
        self._handle_return()
    

    def _run_cards(self):
        try:
            self._card = self._session_set[self._card_nr]
            self._display_card()
        except:
            self._display_end()

    def _create_session_set(self, amount):
        return random.sample(self._pile, amount)


    def _handle_next(self):
        self.destroy()
        self._card_nr += 1
        self._run_cards()


    def _display_card(self):
        self._character = self._canvas.create_text(
            400, 150, 
            text=self._card.character(),
            font=("Arial", 80, "bold"))


        result_title = self._canvas.create_text(
            400, 250, 
            text=self._card.meaning(), 
            font=("Arial", 24))


        next_button = Button(
            self._root,
            text="Next",
            highlightbackground=self._bg_color,
            command=self._handle_next
        )

        button_window = self._canvas.create_window(
            400, 350, 
            window=next_button)

        cards_left = self._canvas.create_text(
            400, 380, 
            text=f'{self._card_nr + 1}/{len(self._session_set)}', 
            font=("Arial", 16))


        

    def _display_end(self):
        self.destroy()

        meaning_title = self._canvas.create_text(
            400, 250, 
            text="End of the set", 
            font=("Arial", 24))

        
        return_button = Button(
          self._root,
          text="Return to menu",
          highlightbackground=self._bg_color,
          command=self._handle_return
        )

        button_window = self._canvas.create_window(
            400, 350, 
            window=return_button)