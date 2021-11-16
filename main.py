from controller import *
from PlayerVsPlayer import *
from PlayerVsComputer import *
from user_strategy import *
from tkinter import *

root = Tk()

strategy = ""


def chooseStrategy(playstyle):
    global strategy
    if playstyle:
        strategy = PlayerVsPlayer()
    else:
        strategy = PlayerVsComputer()
    root.destroy()


if __name__ == "__main__":
    Label(root, text="Choose your playstyle:\n", ).grid(row=0)
    Button(root, text="Player vs Player", command=lambda: chooseStrategy(True)).grid(column=0, row=1)
    Button(root, text="Player vs Computer", command=lambda: chooseStrategy(False)).grid(column=1, row=1)
    mainloop()

    c = Controller(strategy)
