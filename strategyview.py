from PlayerVsPlayer import *
from PlayerVsComputer import *
from user_strategy import *
from tkinter import *
from PlayerVsPlayer import *
from PlayerVsComputer import *


class StrategyView(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.label = Label(self, text="Choose your playstyle:\n", ).grid(row=0)
        self.button_playervsplayer = Button(self, text="Player vs Player",
                                            command=lambda: self.chooseStrategy(True)).grid(column=0, row=1)
        Button(self, text="Player vs Computer", command=lambda: self.chooseStrategy(False)).grid(column=1, row=1)

    def chooseStrategy(self, playstyle):
        if playstyle:
            self.strategy = PlayerVsPlayer()
        else:
            self.strategy = PlayerVsComputer()
        self.quit()
