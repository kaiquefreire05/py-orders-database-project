# main.py
from views.main_view import MainView
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = MainView(root)
    root.mainloop()
