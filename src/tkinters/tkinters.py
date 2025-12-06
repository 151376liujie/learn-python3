from tkinter import Tk
from tkinter import Grid
from tkinter import Button
from tkinter import mainloop
import sys


def onclick():
    print("i am clicked.")


if __name__ == '__main__':
    t = Tk()
    g = Grid()
    for i in range(10):
        # Button(text="button1", command=onclick).pack()
        btn = Button(master=t, cnf={"text": "my button"})
        btn.grid()
    mainloop()
