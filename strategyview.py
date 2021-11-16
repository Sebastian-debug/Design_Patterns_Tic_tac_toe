from PlayerVsPlayer import *
from PlayerVsComputer import *
from user_strategy import *
from tkinter import *
from PlayerVsPlayer import *
from PlayerVsComputer import *


class StrategyView(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Game Mode")
        self.geometry("410x410")
        self.configure(bg="black")
        self.resizable(0, 0)
        self.columnconfigure(0, weight=3)
        self.rowconfigure(1, weight=1)
        self.label_playstyle = Label(master=self, bg='gray', text=f"Choose your playstyle:", height=5, width=35, anchor=CENTER,
                           font=('Helvetica', 14, 'bold'))
        self.label_playstyle.grid(column=0, row=0)
        self.label_playstyle.place(x=0, y=0)
        button_player = Button(self, text="Player vs Player", command=lambda: self.chooseStrategy(True), bg='green',
                               width=16, height=13,
                               anchor=CENTER, font=('Helvetica', 16, 'bold'))
        button_player.grid(column=0, row=1)
        button_player.place(x=0, y=100)
        button_computer = Button(self, text="Player vs Computer", command=lambda: self.chooseStrategy(False), bg='red',
                                 width=16, height=13,
                                 anchor=CENTER, font=('Helvetica', 16, 'bold'))
        button_computer.grid(column=1, row=1)
        button_computer.place(x=200, y=100)

    def chooseStrategy(self, playstyle):
        if playstyle:
            self.strategy = PlayerVsPlayer()
        else:
            self.strategy = PlayerVsComputer()
        self.quit()
