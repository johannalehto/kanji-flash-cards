from tkinter import *
from services.ui_service import UIService


class MenuGUI:
    """Display for the main page of the app."""
    def __init__(self, root, handle_learn, handle_review):
        """Class constructor. Creates a class for the main page.

        Args:
            _root:
                TKinter-element where the Main menu UI is initialized.
        """
        self._root = root
        self._ui_service = UIService()
        self._bg_color = self._ui_service.bg_color
        self._canvas = self._ui_service.initialize_canvas(self._root)
        self._handle_review = handle_review
        self._handle_learn = handle_learn

        self._display_menu()


    def _display_menu(self):
        menu_title = self._canvas.create_text(
            400, 250, 
            text="::KANJI FLASH CARDS::", 
            font=("Arial", 24))


        learn_button = Button(
            self._root,
            text="Learn a set",
            highlightbackground=self._bg_color,
            command=self._handle_learn
        )

        button_window = self._canvas.create_window(
            400, 350,
            window=learn_button)

        review_button = Button(
            self._root,
            text="Review a set",
            highlightbackground=self._bg_color,
            command=self._handle_review
        )

        button_window = self._canvas.create_window(
            400, 400, 
            window=review_button)





    def pack(self):
        """"Displays the view"""
        self._canvas.pack()

    def destroy(self):
        """"Destroys the view"""
        self._canvas.delete('all')





