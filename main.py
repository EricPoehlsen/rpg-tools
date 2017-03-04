import tkinter as tk
import application as a


def main():
    window = tk.Tk()
    app = a.Application(window)
    app.pack()
    window.mainloop()

if __name__ == "__main__":
    main()
