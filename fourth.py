from tkinter import *

class FourthClass:

    def __init__(self):
        self.win = Tk()
        self.win.geometry("800x600")

    def add_widget(self):
        self.mainFrame = Frame(self.win, width=600, height=400, bg="red")
        self.mainFrame.place(x=100, y=100)
        self.win.mainloop()

obj = FourthClass()
obj.add_widget()