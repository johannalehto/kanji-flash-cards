from tkinter import *
class UIService:

    def _initialize(self):
        """"Initializes the UI view"""
        self._canvas = Canvas(self._root, width=800, height=526)
        self._canvas.config(bg="#fff", highlightthickness=0)
        self._canvas.grid(row=0, column=0, columnspan=2)

    def pack(self):
        """"Displays the view"""
        self._canvas.pack()

    def destroy(self):
        """"Destroys the whole view"""
        self._canvas.delete('all')

    