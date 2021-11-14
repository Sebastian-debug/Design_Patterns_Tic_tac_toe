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

        choice = self.model.user_choice(self.view.entry1.get())
        if choice == -1:
            self.view.label10['text'] = "Invalid! [1-9] Pick [U] Undo [R] Redo [N] New\n  [L] Load [S] Save"
            return
        if choice == -2:
            global buffer
            buffer = ["Ä", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            player_count = 1
            global current_line_history
            current_line_history = 0
            self.model.new_history_file()
            self.view.display(self.model.buffer, self.model.current_line_history)
            self.view.entry1.delete(0, END)
            return
        if choice == -3:
            self.model.load_game()
            self.view.display(self.model.buffer, self.model.current_line_history)
            self.view.entry1.delete(0, END)
            return
        if choice == -4:
            self.model.save_game()
            self.view.display(self.model.buffer, self.model.current_line_history)
            self.view.entry1.delete(0, END)
            return

        self.model.set_marker(player_marker, choice)
        self.view.display(self.model.buffer, self.model.current_line_history)
        win_check_ret = self.model.win_check(player_marker, self.player_count)
        if win_check_ret:
            self.view.label10["text"] = win_check_ret
            self.view.display(self.model.buffer, self.model.current_line_history)
            pass
        else:
            self.view.display(self.model.buffer, self.model.current_line_history)
            self.view.label10['text'] = "[1-9] Pick [U] Undo [R] Redo [N] New\n  [L] Load [S] Save"

        if self.player_count == 1:
            self.player_count = 2
            self.view.label11["text"] = "Player O"
            self.view.label11["bg"] = "pink"
        else:
            self.player_count = 1
            self.view.label11["text"] = "Player X"
            self.view.label11["bg"] = "green"

        self.view.entry1.delete(0, END)
