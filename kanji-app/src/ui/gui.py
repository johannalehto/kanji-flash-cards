from tkinter import *
from ui.menu_gui import MenuGUI
from ui.review_gui import ReviewGUI

BACKGROUND_COLOR = "#fff"
word_file = "./src/data/default.csv"


class GUI:
    def __init__(self, root):
        """Class constructor. Creates a class for the UI.

        Args:
            root:
                TKinter-element where the UI is initialized.
            current_view:
                TKinter-element for currently displayed view.

        """
        self._root = root
        self._canvas = None
        self._current_view = None


    def _initialize(self):
        """"Initializes the UI view"""
        self._canvas = Canvas(self._root, width=800, height=526)
        self._canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self._canvas.grid(row=0, column=0, columnspan=2)

    def start(self):
        """Starts the UI."""
       # self._show_menu_view()
        self._show_review_view(self._canvas)

    # def _show_menu_view(self):
    #     """Displays the main page."""
    #     self._hide_current_view()

    #     self._current_view = MenuGUI(
    #         self._root,
    #     #    self._show_learn_view,
    #         self._show_review_view,    
    #     )

    #     self._current_view.pack()

    def _hide_current_view(self):
        """Destroys the current view before displaying new view."""
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_review_view(self):
        """Displays Review of the cards."""
        self._hide_current_view()

        self._current_view = ReviewGUI(self._root, self._show_review_view)
        self._current_view.pack()












