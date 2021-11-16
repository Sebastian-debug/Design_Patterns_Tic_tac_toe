from model import *
from constants import *
from view import *
from strategyview import *


class Controller:
    def __init__(self):
        self.model = Model()
        self.strategy_view = StrategyView()
        self.strategy_view.mainloop()
        print(self.strategy_view.strategy)
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
            print("HALLO")
            return

        self.model.handle_valid_move(choice)

        self.model.player_count = self.strategy.strategy(self.model.player_count)
