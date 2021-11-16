from model import *
from constants import *
from view import *
from strategyview import *


class Controller:
    def __init__(self):
        self.model = Model()
        self.strategy_view = StrategyView()
        self.strategy_view.mainloop()
        self.strategy = self.strategy_view.strategy
        self.strategy_view.destroy()
        self.view = View(self.model)
        self.model.createFile()
        self.view.bind('<Return>', self.onEnter)
        self.view.mainloop()
        self.model.detach(self.view)

    def onEnter(self, event=None):
        choice = self.model.user_choice(self.view.user_entry.get())

        if choice == INVALID or choice == NEW_GAME or choice == LOAD_GAME or choice == SAVE_GAME:
            if choice == LOAD_GAME or choice == NEW_GAME:
                self.model.checkIfAlreadyWon()
            return

        if isinstance(self.strategy, PlayerVsComputer) and (choice == UNDO or choice == REDO):
            self.model.checkIfAlreadyWon()
            return

        self.model.set_marker(choice, False)
        self.model.checkIfAlreadyWon()

        if not (isinstance(self.strategy, PlayerVsComputer) and self.model.win_check(PLAYER_X_MARKER)):
            self.model.player_count = self.strategy.strategy(self.model.player_count)
