from tkinter import *
from ui.menu_gui import MenuGUI
from ui.review_gui import ReviewGUI
from ui.learn_gui import LearnGUI


class GUI:
    def __init__(self, root, word_file):
        """Class constructor. Creates a class for the UI.

        Args:
            _root:
                TKinter-element where the UI is initialized.
            _current_view:
                TKinter-element for currently displayed view.
            _word_file:
                File name for creating the list of words for session.

        """
        self._root = root
        self._current_view = None
        self._wordfile = word_file

    def start(self):
        """Starts the UI."""
        self._show_menu_view()

    def _show_menu_view(self):
        """Displays the main page."""
        self._hide_current_view()

        self._current_view = MenuGUI(
            self._root,
            self._show_learn_view,
            self._show_review_view,
        )

    def _show_learn_view(self):
        """Displays Learn view of the cards."""
        self._hide_current_view()

        self._current_view = LearnGUI(
            self._root,
            self._wordfile,
            self._show_menu_view)

    def _show_review_view(self):
        """Displays Review of the cards."""
        self._hide_current_view()

        self._current_view = ReviewGUI(
            self._root,
            self._wordfile,
            self._show_menu_view,
        )

    def _hide_current_view(self):
        """Destroys the current view before displaying new view."""
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None
