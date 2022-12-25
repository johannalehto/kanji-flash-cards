from tkinter import *


class MenuGUI:
    """Display for the main page of the app."""

    def __init__(self, root, handle_learn, handle_review):
        """Class constructor. Creates a class for the main page.

        Args:
            _root:
                TKinter-element where the Main menu UI is initialized.
        """
        self._root = root
        self._bg_color = "#fff"
        self._canvas = None
        self._handle_review = handle_review
        self._handle_learn = handle_learn

        self.initialize_canvas()
        self._display_menu()

    def initialize_canvas(self):
        """"Initializes the UI view"""
        self._canvas = Canvas(self._root, width=800, height=526)
        self._canvas.config(bg="#fff", highlightthickness=0)
        self._canvas.grid(row=0, column=0, columnspan=2)

    def _display_menu(self):
        """"Displays the menu with feature options"""
        menu_title = self._canvas.create_text(
            400, 150,
            text="::KANJI FLASH CARDS::",
            font=("Arial", 24))

        learn_button = Button(
            self._root,
            text="Learn a set",
            highlightbackground=self._bg_color,
            command=self._handle_learn
        )

        button_window = self._canvas.create_window(
            400, 250,
            window=learn_button)

        review_button = Button(
            self._root,
            text="Review a set",
            highlightbackground=self._bg_color,
            command=self._handle_review
        )

        button_window = self._canvas.create_window(
            400, 300,
            window=review_button)

    def destroy(self):
        """"Destroys the view"""
        self._canvas.delete('all')
