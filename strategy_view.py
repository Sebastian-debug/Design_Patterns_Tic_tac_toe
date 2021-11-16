from tkinter import *
from player_vs_player import *
from player_vs_computer import *


class StrategyView(Tk):
    """
    A class to represent the view for choosing the game mode.

    Attributes
    ----------
    Methods
    -------
    chooseStrategy(playstyle):
        user can choose the different game modes

    """
    def __init__(self):
        Tk.__init__(self)
        self.title("Game Mode")
        self.geometry("410x410")
        self.configure(bg="black")
        self.resizable(0, 0)
        self.columnconfigure(0, weight=3)
        self.rowconfigure(1, weight=1)
        self.label_playstyle = Label(master=self, fg='white', bg='grey1', text=f"Choose your playstyle:", height=4,
                                     width=31, anchor=CENTER,
                                     font=('Bookman Old Style', 14, 'bold'))
        self.label_playstyle.grid(column=0, row=0)
        self.label_playstyle.place(x=0, y=0)
        button_player = Button(self, text="Player vs Player", fg='white', command=lambda: self.chooseStrategy(True),
                               bg='blue1',
                               width=15, height=12,
                               anchor=CENTER, font=('Bookman Old Style', 14, 'bold'))
        button_player.grid(column=0, row=1)
        button_player.place(x=0, y=95)
        button_computer = Button(self, text="Player vs Computer", fg='white',
                                 command=lambda: self.chooseStrategy(False), bg='red1',
                                 width=15, height=12,
                                 anchor=CENTER, font=('Bookman Old Style', 14, 'bold'))
        button_computer.grid(column=1, row=1)
        button_computer.place(x=210, y=95)

    def chooseStrategy(self, playstyle):
        """
        Updates the markers of the players according to the current turn
        Parameters
        ----------
        playstyle : bool
            The game mode
        Returns
        -------
        """
        if playstyle:
            self.strategy = PlayerVsPlayer()
        else:
            self.strategy = PlayerVsComputer()
        self.quit()
