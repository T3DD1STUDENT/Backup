import os,time,ttkbootstrap as ttk, tkinter as tk
from tkinter import messagebox


class List(ttk.Window):
    def __init__ (self):
        super().__init__(themename='journal')
        self.title("Todolist")
        self.geometry("400x300")
        self.resizable(False, False)
        self.notebook=ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")
        self.buatTab( "Tab 1","List Maker")
    def buatTab(self, judul, kontentext):
        tab = ttk.Frame(self.notebook)
        label = ttk.Label(tab, text=kontentext, padding=20)
        label.pack(fill="both", expand=True)
        self.notebook.add(tab, text=judul)
    class ListMaking:
        def __init__ (self):
            super().__init__()
if __name__ == "__main__":
    app = List()
    app.mainloop()