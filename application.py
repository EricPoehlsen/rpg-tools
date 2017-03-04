import tkinter as tk
import labyrinth


class Application(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)

        self.window = window
        self.showMenu()
        self.showLabyrinth()

    def showMenu(self):
        menu = tk.Menu(self.window)
        file = tk.Menu(menu, tearoff=0)
        file.add_command(label="New ...")
        file.add_command(label="Quit", command=self.window.quit)
        menu.add_cascade(label="File", menu=file)

        self.window.config(menu=menu)

    def showLabyrinth(self):
        self.clear()
        l = labyrinth.Labyrinth(self)
        l.pack()

    def clear(self):
        widgets = self.winfo_children()
        for widget in widgets:
            widget.destroy()
