from view import *
from model import *

class Controller(object):
    def __init__(self):
        self.player_count = 1
        self.file_name = "history.txt"
        self.view = View()
        self.model = Model(self.file_name)
        self.model.createFile()
        self.view.bind('<Return>', self.onEnter)
        self.view.mainloop()
        #hallo = self.view.label_marker_list.get()

    def onEnter(self, event=None):
        if self.player_count == 1:
            player_marker = "X"
        else:
            player_marker = "O"

        choice = self.model.user_choice(self.view.user_entry.get())
        if choice == -1:
            self.view.label_start['text'] = "Invalid! [1-9] Pick [U] Undo [R] Redo [N] New\n  [L] Load [S] Save"
            return
        if choice == -2:
            self.model.buffer = ["Ä", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            self.player_count = 1
            self.model.current_line_history = 0
            self.model.createFile()
            self.view.display(self.model.buffer, self.model.current_line_history)
            self.view.user_entry.delete(0, END)
            return
        if choice == -3:
            self.player_count = 1 if self.model.load_game() else 2
            self.view.display(self.model.buffer, self.model.current_line_history)
            self.view.user_entry.delete(0, END)
            return
        if choice == -4:
            self.model.save_game()
            self.view.display(self.model.buffer, self.model.current_line_history)
            self.view.user_entry.delete(0, END)
            return

        self.model.set_marker(player_marker, choice)
        self.view.display(self.model.buffer, self.model.current_line_history)
        win_check_ret = self.model.win_check(player_marker, self.player_count)
        if win_check_ret:
            self.view.label_start["text"] = win_check_ret
            self.view.display(self.model.buffer, self.model.current_line_history)
            pass
        else:
            self.view.display(self.model.buffer, self.model.current_line_history)
            self.view.label_start['text'] = "[1-9] Pick [U] Undo [R] Redo [N] New\n  [L] Load [S] Save"

        if self.player_count == 1:
            self.player_count = 2
            self.view.label_players["text"] = "Player O"
            self.view.label_players["bg"] = "pink"
        else:
            self.player_count = 1
            self.view.label_players["text"] = "Player X"
            self.view.label_players["bg"] = "green"

        self.view.user_entry.delete(0, END)
