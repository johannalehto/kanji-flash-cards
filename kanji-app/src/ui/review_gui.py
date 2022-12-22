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
        self._canvas = None
        self._character = None
        self._meaning_entry = None
        self._next_button = None
        self._card = None
        self._viewed  = []

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

        self._initialize_card()

        self._card = self._give_a_card()
        self._canvas.itemconfig(self._character, text=self._card.character(), fill="black")
        self._meaning_entry.bind('<Return>', self._handle_answer)
        # self._meaning_entry.bind('<Return>', self._clear, add="+")  


    def _give_a_card(self):
        # card = random.choice(self._pile)
        # if card not in self._viewed:
        #     self._viewed.append(card)
        #     return card
        return random.choice(self._pile)
        

    def _handle_answer(self, event):
        """"Checks whether answer is correct from the service"""
        answer = self._meaning_entry.get()
        print(answer)
        if self._service.check_meaning(answer, self._card):
            self._result("Correct")
        else:
            self._result("Wrong")

    def _result(self, result: str):
        result_title = self._canvas.create_text(
            400, 350, 
            text=result, 
            font=("Arial", 24))

    def _handle_next(self):
        self.destroy()
        self._run_cards()
        

    def _initialize_card(self):
        self._character = self._canvas.create_text(
            400, 150, 
            text="漢字", 
            font=("Arial", 80, "bold"))

        meaning_title = self._canvas.create_text(
            400, 250, 
            text="meaning:", 
            font=("Arial", 24))

        self._meaning_entry = Entry(
            self._root,
            font=("Arial", 24), 
            width=34, 
            fg="#000")

        entry_window = self._canvas.create_window(
            400, 300, 
            window=self._meaning_entry)

        next_button = Button(
          self._root,
          text="Next",
          command=self._handle_next
        )

        button_window = self._canvas.create_window(
            400, 330, 
            window=next_button)








