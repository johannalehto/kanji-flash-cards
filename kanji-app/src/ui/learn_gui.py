from tkinter import *
from services.kanji_service import KanjiService
import random


class LearnGUI:
    """Display for reviewing the cards."""

    def __init__(self, root, word_file, handle_return):
        """Class constructor. Creates a class for the learning view.

        Args:
            _root:
                TKinter-element where the Review UI is initialized.
            _service:
                For accessing methods from KanjiService-object.
            _bg_color:
                Common background color code for the view.
            _pile:
                Receives a new set of cards.
            _session_set:
                Creates a set of desired amount for the round.
            _canvas:
                Creates structure for the visual elements.
           _handle_return:
                Value called after the end of the set for returning to main menu.
            _character:
                Holds character in display.
            _card_nr:
                Current card index.
            _card:
                Holds current card in display.
        """

        self._root = root
        self._service = KanjiService()
        self._bg_color = "#fff"
        self._pile = self._service.create_cardset_from_file(word_file)
        self._session_set = self._create_session_set(amount=5)
        self._canvas = None
        self._handle_return = handle_return
        self._character = None
        self._card_nr = 0
        self._card = None

        self.initialize_canvas()
        self._run_cards()

    def initialize_canvas(self):
        """"Initializes the UI view"""
        self._canvas = Canvas(self._root, width=800, height=526)
        self._canvas.config(bg="#fff", highlightthickness=0)
        self._canvas.grid(row=0, column=0, columnspan=2)

    def destroy(self):
        """"Destroys the view"""
        self._canvas.delete('all')

    def _return_handler(self):
        """"Responsible for returning to the menu view"""
        self._handle_return()

    def _run_cards(self):
        """"Displays each card from the set one at a time"""
        try:
            self._card = self._session_set[self._card_nr]
            self._display_card()
        except:
            self._display_end()

    def _create_session_set(self, amount):
        """"Creates a set of cards based on desired amount"""
        return random.sample(self._pile, amount)

    def _handle_next(self):
        """"Cleans up the card view and calls for a next card"""
        self.destroy()
        self._card_nr += 1
        self._run_cards()

    def _display_card(self):
        """"Responsible for displaying the kanji-character 
            and the title for meaning"""
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
        """"Responsible for displaying the end page
            after all cards are run"""
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
