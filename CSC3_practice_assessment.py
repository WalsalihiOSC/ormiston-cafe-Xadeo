#Coding of the cafe interface for ormiston
from tkinter import *

class menu:
    def __init__(self):
        self.first_image = PhotoImage(file = "Pictures/tuckshoplogo.png")


class cafeinterface:
    def __init__(self, parent):

        


#main routine
if __name__ == "__main__":
    root = Tk()
    cafe = cafeinterface(root)
    root.mainloop()