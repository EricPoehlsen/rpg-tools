import tkinter as tk
import numpy as np
import random

EAST = 0b0001
SOUTH = 0b0010
WEST = 0b0100
NORTH = 0b1000


class Labyrinth(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.window = window
        self.canvas = tk.Canvas(self.window, width=500, height=500)
        self.canvas.pack()

        self.labyrinth = np.zeros((10, 10))

    def createCell(self, entry):
        doors = random.randint(0b0000, 0b1111)
        doors = doors | entry
