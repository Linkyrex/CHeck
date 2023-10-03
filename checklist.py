'''
This file contains the Checklist class which represents the table-like interface of the Ccheck app.
'''
import tkinter as tk
from item import Item
class Checklist(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.items = []
        self.table = tk.Frame(self)
        self.table.pack()
        self.add_item_button = tk.Button(self, text="Add Item", command=self.add_item)
        self.add_item_button.pack()
    def add_item(self):
        item = Item(self.table)
        item.pack()
        self.items.append(item)