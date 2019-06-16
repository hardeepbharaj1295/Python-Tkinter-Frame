from tkinter import *
from second import MainClass

class SixthClass:

    def __init__(self):
        self.win = Tk()
        self.win.geometry("400x200")

    def add_widget(self):
        self.mainFrame = Frame(self.win)
        self.mainFrame.place(x=100, y=50)

        self.label = Label(self.mainFrame, text="Username : ")
        self.label.grid(row=0, column=0)

        self.username = Entry(self.mainFrame)
        self.username.grid(row=0, column=1)

        self.button = Button(self.mainFrame, text="Submit", command=self.changeFrame)
        self.button.grid(row=1, column=1)

        self.win.mainloop()

    def changeFrame(self):
        self.win.destroy()
        s = MainClass()

if __name__ == "__main__":
    obj = SixthClass()
    obj.add_widget()