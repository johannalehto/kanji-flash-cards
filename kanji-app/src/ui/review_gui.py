from tkinter import *
from services.kanji_service import KanjiService

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
        self._card = None

        self._initialize()

    def pack(self):
        """"Displays the view"""
        self._canvas.pack()

    # def destroy(self):
    #     """"Destroys the view"""
    #     self._canvas.delete('all')

    def _return_handler(self):
        """"Responsible for returning to the menu view"""
        self._handle_return()

    def _handle_answer(self):
        """"Checks whether answer is correct from the service"""
        answer = self._card_meaning_entry.get()
        if self._service.check_meaning(answer, self._card):
            self._result("Correct")
        else:
            self._result("Wrong")

    def _result(self, result: str):
        result_title = self._canvas.create_text(
            400, 350, 
            text=result, 
            font=("Arial", 24))


    def _initialize(self):
        """"Initializes the card round view"""
        self._canvas = Canvas(self._root, width=800, height=526)
        self._canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self._canvas.grid(row=0, column=0, columnspan=2)
  
        self._initialize_card()
        self._initialize_entry()

        for card in self._pile:
            self._card = card
            self._canvas.itemconfig(self._character, text=self._card.character(), fill="black")
           # self._meaning_entry.bind('<Return>', self._handle_answer())   
            breakpoint()
            self._handle_next()
    

    def _handle_next(self):
        pass
        

    def _initialize_card(self):
        self._character = self._canvas.create_text(
            400, 150, 
            text="漢字", 
            font=("Arial", 80, "bold"))

    
    def _initialize_entry(self):
        _meaning_title = self._canvas.create_text(
            400, 250, 
            text="meaning:", 
            font=("Arial", 24))

        _meaning_entry = Entry(
            self._root,
            font=("Arial", 24), 
            width=34, 
            fg="#000")

        
        # _button = Button(
        #   master=self._frame,
        #   text="Check",
        #   command=self._handle_answer()
        # )

       # _meaning_entry.grid(row=1, column=1)

        _entry_window = self._canvas.create_window(
            400, 300, 
            window=_meaning_entry)

 

        # _button_window = self._canvas.create_window(
        #     400, 330, 
        #     window=_button)





