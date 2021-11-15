from model import *
from constants import *
from view import *
from PlayerVsPlayer import *
from PlayerVsComputer import *


class Controller:
    def __init__(self, strategy):
        self.model = Model()
        self.view = View(self.model)
        self.model.createFile()
        self.view.bind('<Return>', self.onEnter)
        self.strategy = strategy
        self.view.mainloop()
        self.model.detach(self.view)

    def onEnter(self, event=None):
        choice = self.model.user_choice(self.view.user_entry.get())

        if choice == INVALID or choice == NEW_GAME or choice == LOAD_GAME or choice == SAVE_GAME:
            print("HALLO")
            return

        self.model.handle_valid_move(choice)

        self.model.player_count = self.strategy.strategy(self.model.player_count)
