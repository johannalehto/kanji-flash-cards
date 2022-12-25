from tkinter import *

class UIService:
    """ Common methods for UI """

    def __init__(self):
        """Class constructor. Creates a class for the UI service.

        Args:
            root:
                TKinter-element where the UI is initialized.
        """
        self.canvas = None
        self.bg_color = "#fff"

    def initialize_canvas(self, root):
        """"Initializes the UI view"""
        self.canvas = Canvas(root, width=800, height=526)
        self.canvas.config(bg="#fff", highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)
        return self.canvas


    