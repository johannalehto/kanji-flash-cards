from tkinter import *
from services.kanji_service import KanjiService
import random

BACKGROUND_COLOR = "#fff"
word_file = "./src/data/default.csv"

class ReviewGUI:
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

            _meaning_entry:
                Holds answer added by the user.

            _card:
                Holds current card in display.
            


        """

        self._root = root
        self._handle_return = handle_return
        self._service = KanjiService()
        self._pile = self._service.create_cardset_from_file(word_file)
        self._session_set = self._create_session_set(amount=5)
        self._canvas = None
        self._character = None
        self._meaning_entry = None
        self._card = None

        self._initialize()
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


    def _initialize(self):
        """"Initializes the card round view"""
        self._canvas = Canvas(self._root, width=800, height=526)
        self._canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self._canvas.grid(row=0, column=0, columnspan=2)
    

    def _run_cards(self):
        try:
            self._card = self._give_a_card()
            self._display_card()
            self._display_entry()
            self._meaning_entry.bind('<Return>', self._display_result)
        except:
            self._display_end()

    def _create_session_set(self, amount):
        return random.sample(self._pile, amount)

    def _give_a_card(self):
        return self._session_set.pop()

    def _handle_answer(self):
        """"Checks whether answer is correct from the service"""
        answer = self._meaning_entry.get()
        print(answer)
        if self._service.check_meaning(answer, self._card):
            return "Correct"
        return "Wrong"


    def _result_color(self, result: str):
        if result == "Correct":
            return "#71E0AB"
        return "#FF7070"


    def _handle_next(self):
        self.destroy()
        self._run_cards()
        

    def _display_card(self):
        self._character = self._canvas.create_text(
            400, 150, 
            text=self._card.character(),
            font=("Arial", 80, "bold"))

        meaning_title = self._canvas.create_text(
            400, 250, 
            text="meaning:", 
            font=("Arial", 24))


    def _display_entry(self):
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
          command=self._handle_next
        )

        next_button.bind('<Return>', self._handle_next)

        button_window = self._canvas.create_window(
            400, 350, 
            window=next_button)

    def _display_end(self):
        self.destroy()

        meaning_title = self._canvas.create_text(
            400, 250, 
            text="End of the set", 
            font=("Arial", 24))

        results_title = self._canvas.create_text(
            400, 350, 
            text=f"points: / ", 
            font=("Arial", 24))
        
        return_button = Button(
          self._root,
          text="Return to menu",
          command=self._return_handler
        )

        button_window = self._canvas.create_window(
            400, 350, 
            window=return_button)













