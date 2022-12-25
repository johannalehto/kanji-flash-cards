from tkinter import *
from services.kanji_service import KanjiService
from entities.session import Session
import random


class ReviewGUI:
    """Display for reviewing the cards."""

    def __init__(self, root, word_file, handle_return):
        """Class constructor. Creates a class for the review.

        Args:
            _root:
                TKinter-element where the Review UI is initialized.
            _kanji_service:
                For accessing methods from KanjiService-object.
            _bg_color:
                Common background color code for the view.
            _pile:
                Receives a new set of cards.
            _session_set:
                Creates a set of desired amount for the round.
            _session:
                Creates an object for keeping up the points.
            _canvas:
                Creates structure for the visual elements.
           _handle_return:
                Value called after the end of the set for returning to main menu.
            _character:
                Holds character in display.
            _meaning_entry:
                Holds answer added by the user.
            _card:
                Holds current card in display.
        """

        self._root = root
        self._kanji_service = KanjiService()
        self._bg_color = "#fff"
        self._pile = self._kanji_service.create_cardset_from_file(word_file)
        self._amount = 5
        self._session_set = self._create_session_set(self._amount)
        self._session = Session()
        self._canvas = None
        self._handle_return = handle_return
        self._character = None
        self._meaning_entry = None
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
            self._card = self._give_a_card()
            self._display_card()
            self._display_entry()
            self._meaning_entry.bind('<Return>', self._display_result)
        except:
            self._display_end()

    def _create_session_set(self, amount):
        """"Creates a set of cards based on desired amount"""
        return random.sample(self._pile, amount)

    def _give_a_card(self):
        """"Returns a card from set and removes it from the set"""
        return self._session_set.pop()

    def _handle_answer(self):
        """"Checks whether answer is correct from the service"""
        answer = self._meaning_entry.get()
        if self._kanji_service.check_meaning(answer, self._card):
            self._session.add_point()
            return "Correct"
        return "Wrong"

    def _result_color(self, result: str):
        """"Returns a color hex according to the result"""
        if result == "Correct":
            return "#71E0AB"
        return "#FF7070"

    def _handle_next(self):
        """"Cleans up the card view and calls for a next card"""
        self.destroy()
        self._run_cards()

    def _display_card(self):
        """"Responsible for displaying the kanji-character 
            and the title for meaning"""
        self._character = self._canvas.create_text(
            400, 150,
            text=self._card.character(),
            font=("Arial", 80, "bold"))

        meaning_title = self._canvas.create_text(
            400, 250,
            text="meaning:",
            font=("Arial", 24))

    def _display_entry(self):
        """"Responsible for displaying the entry form"""
        self._meaning_entry = Entry(
            self._root,
            font=("Arial", 24),
            width=24,
            justify="center",
            fg="#000")

        self._meaning_entry.focus_set()

        entry_window = self._canvas.create_window(
            400, 300,
            window=self._meaning_entry)

    def _display_result(self, event):
        """"Responsible for displaying the result 
            after user entry"""
        answer = self._meaning_entry.get()
        result = self._handle_answer()
        color = self._result_color(result)

        self._meaning_entry.destroy()

        rect = self._canvas.create_rectangle(
            245, 280, 556, 316,
            outline=color,
            fill=color)

        result_title = self._canvas.create_text(
            400, 300,
            text=answer,
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

    def _display_end(self):
        """"Responsible for displaying the end page
            after all cards are run"""

        self.destroy()

        meaning_title = self._canvas.create_text(
            400, 250,
            text="End of the set",
            font=("Arial", 24))

        results_title = self._canvas.create_text(
            400, 300,
            text=f"You got {self._session.session_points()} / {self._amount} correct",
            font=("Arial", 24))

        return_button = Button(
            self._root,
            highlightbackground=self._bg_color,
            text="Return to menu",
            command=self._handle_return
        )

        button_window = self._canvas.create_window(
            400, 350,
            window=return_button)
