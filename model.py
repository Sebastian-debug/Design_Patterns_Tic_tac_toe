import os
import shutil
import easygui
import linecache
from view import *


class Model:
    singleton_instance = None

    @staticmethod
    def getInstance():
        if Model.singleton_instance is None:
            return Model()
        else:
            return Model.singleton_instance

    def __init__(self):
        if Model.singleton_instance is not None:
            raise Exception("There can only be one instance of Model")
        else:
            Model.singleton_instance = self
        self.file_name = "history.txt"
        self.current_line_history = 0
        self.buffer = ["Ä", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def createFile(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
        open(self.file_name, "a")
        self.history_file()

    def history_file(self):
        with open(self.file_name, "a+") as file:
            if self.current_line_history != self.get_file_line_numbers(self.file_name):
                file.seek(0)
                tmp_history_lines = file.readlines()
                file.seek(0)
                file.truncate()
                for line in tmp_history_lines[:self.current_line_history]:
                    file.write(line)

            for field in self.buffer[1:]:
                if field == " ":
                    file.write(" ")
                elif field == "X":
                    file.write("X")
                else:
                    file.write("O")
            file.write("\n")

        self.current_line_history += 1

    def get_file_line_numbers(self, file):
        return sum(1 for _ in open(file))

    def user_choice(self, choice):
        acceptable_range = range(1, 10)
        if not choice.isdigit():
            if choice == "U":
                if self.current_line_history == 1:
                    return -1
                self.undo(False)
                return 0
            if choice == "R":
                return -1 if self.undo(True) == -1 else 0
            if choice == "N":
                return -2
            if choice == "L":
                return -3
            if choice == "S":
                return -4
            return -1
        elif int(choice) not in acceptable_range:
            return -1
        if not self.free_space_check(choice):
            return -1
        return int(choice)

    def load_game(self):
        file_name_loaded_game = easygui.fileopenbox()
        self.file_name = file_name_loaded_game
        open(self.file_name, "a")

        linecache.clearcache()
        last_line_new_file = linecache.getline(self.file_name, self.get_file_line_numbers(self.file_name))

        for line_index in range(len(last_line_new_file)):
            if line_index + 1 < len(self.buffer) and last_line_new_file[line_index] != "\n":
                self.buffer[line_index + 1] = last_line_new_file[line_index]

        self.current_line_history = self.get_file_line_numbers(self.file_name)
        return True if self.current_line_history % 2 else False

    def save_game(self):

        saved_file_name = easygui.filesavebox(filetypes=['*.txt'])

        if saved_file_name[-4:] != ".txt":
            saved_file_name += ".txt"

        try:
            shutil.copyfile(self.file_name, saved_file_name)
        except shutil.SameFileError:
            pass

    def set_marker(self, marker, position):
        if position == 0:
            return
        self.buffer[position] = marker
        self.history_file()

    def win_check(self, mark, current_player):
        win_pos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for x in win_pos:
            check = True
            for y in x:
                if self.buffer[y] != mark:
                    check = False
                    break
            if check:
                # self.view.label10['text'] = "Player " + str(current_player) + " won the Game!"
                return "Player " + str(current_player) + " won the Game!"
        if " " not in self.buffer:
            # self.view.label10['text'] = "DRAW!"
            return "DRAW!"
        return False

    def free_space_check(self, position):
        return True if self.buffer[int(position)] == " " else False

    def undo(self, redo):
        file_to_game = self.file_name

        if redo:
            self.current_line_history += 1
            if self.get_file_line_numbers(self.file_name) < self.current_line_history:
                self.current_line_history -= 1
                print("Cannot redo, there are no steps ahead!")
                return -1
        else:
            self.current_line_history -= 1

        linecache.clearcache()
        undo_history_line = linecache.getline(file_to_game, self.current_line_history)

        for index, marker in enumerate(undo_history_line):
            if len(self.buffer) != index + 1:
                self.buffer[index + 1] = marker
