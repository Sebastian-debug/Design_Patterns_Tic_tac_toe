from model import *
from constants import *
from view import *
from PlayerVsPlayer import *
from PlayerVsComputer import *


class Controller():
    def __init__(self, strategy):
        self.player_count = PLAYER_X_MARKER
        self.model = Model()
        self.view = View(self.model)
        self.model.createFile()
        self.view.bind('<Return>', self.onEnter)
        self.strategy = strategy
        self.view.mainloop()
        self.model.detach(self.view)


    def onEnter(self, event=None):
        if self.player_count == PLAYER_X_MARKER:
            player_marker = "X"
        else:
            player_marker = "O"

        choice = self.model.user_choice(self.view.user_entry.get())
        if choice == INVALID:
            self.view.label_start['text'] = "Invalid! [1-9] Pick [U] Undo [R] Redo [N] New\n  [L] Load [S] Save"
            return
        if choice == NEW_GAME:
            self.model.buffer = ["Ä", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            self.player_count = PLAYER_X_MARKER
            self.model.current_line_history = 0
            self.model.createFile()
            self.view.display(self.model.buffer, self.model.current_line_history)
            self.view.user_entry.delete(0, END)
            return
        if choice == LOAD_GAME:
            self.player_count = PLAYER_X_MARKER if self.model.load_game() else PLAYER_O_MARKER
            self.view.display(self.model.buffer, self.model.current_line_history)
            self.view.user_entry.delete(0, END)
            return
        if choice == SAVE_GAME:
            self.model.save_game()
            self.view.display(self.model.buffer, self.model.current_line_history)
            self.view.user_entry.delete(0, END)
            return

        self.model.set_marker(player_marker, choice)
        self.view.display(self.model.buffer, self.model.current_line_history)
        win_check_ret = self.model.win_check(player_marker, PLAYER_X_MARKER if self.player_count else PLAYER_O_MARKER)
        if win_check_ret:
            self.view.label_start["text"] = win_check_ret
            self.view.display(self.model.buffer, self.model.current_line_history)
            pass
        else:
            self.view.display(self.model.buffer, self.model.current_line_history)
            self.view.label_start['text'] = "[1-9] Pick [U] Undo [R] Redo [N] New\n  [L] Load [S] Save"

        self.player_count, self.view.label_players["text"], self.view.label_players["bg"] = \
            self.strategy.strategy(self.player_count)
        self.view.display(self.model.buffer, self.model.current_line_history)

        self.view.user_entry.delete(0, END)
