# TODO : 1 first import the tkinter module
from tkinter import *

# TODO : 2 create class (MainClass)
class MainClass:

    # TODO : 3 create constructor
    def __init__(self):
        # TODO : 4 To create a main window , tkinter offers a method TK()
        self.main = Tk()

        # TODO : 5 mainloop() method is used when your application is ready to run
        self.main.mainloop()

# TODO : 6 call to MainClass constructor
x = MainClass()