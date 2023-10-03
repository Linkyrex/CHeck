'''
This file contains the ChecklistItem class which represents an item in the Ccheck app.
'''
import tkinter as tk
class ChecklistItem(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(side=tk.LEFT)
        self.notes_entry = tk.Entry(self)
        self.notes_entry.pack(side=tk.LEFT)
        self.checkboxes = []
        self.create_checkbox("State A")
        self.create_checkbox("State B")
    def create_checkbox(self, text):
        checkbox = tk.Checkbutton(self, text=text)
        checkbox.pack(side=tk.LEFT)
        self.checkboxes.append(checkbox)