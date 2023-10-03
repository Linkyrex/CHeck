'''
This is the main file of the Ccheck checklist app. It contains the main function to run the application.
'''
import tkinter as tk
from checklist import Checklist
def main():
    root = tk.Tk()
    root.title("Ccheck")
    checklist = Checklist(root)
    checklist.pack()
    root.mainloop()
if __name__ == "__main__":
    main()