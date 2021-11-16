import os
import shutil
import easygui
import linecache
from constants import *
from observer import *


class Model(Subject):
    """
    A class to represent the model and the concrete subject.
    The concrete subject is used for the state, attach, detach and notify method
    In addition the model includes the business logic of the game.

    Attributes
    ----------
    singleton_instance : Model
        The instance of the model
    state : str
        The subject state
    observers: list()
        List of all observers

    Methods
    -------
    getInstance():
        Returns instance of model
    attach(observer):
        Attaches the observer to the observers list
    detach(observer):
        Detaches the observer from the observers list
    notify():
        Notifies the observers to update
    createFile():
        Creates new .txt file, which is used to store the game moves
    history_file():
        Writes game moves to the storage file
    get_file_line_numbers(file):
        Returns the line numbers of the given file
    invalid_label():
        Notifies the observer for an invalid move
    valid_label():
        Notifies the observer for an valid move
    user_choice(choice):
        Handles the input of the user
    load_game():
        Used to load an old game
    save_game():
        Used to saved the current game as .txt file
    set_marker(position, computer):
        Used to update the current game field
    win_check(current_player):
        To check the winning condition of the game
    free_space_check(position):
        To check if the chosen position is empty
    undo(redo):
        To undo and redo the current game moves
    checkIfAlreadyWon():
        Checks the win condition for both players

    """
    singleton_instance = None
    state = ""
    observers = list()

    @staticmethod
    def getInstance():
        """
        Returns instance of model

        Parameters
        ----------

        Returns
        -------
        Model.singleton_instance : Model
            The instance of the model
        """
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
        self.info_label = VALID_INPUT
        self.current_player_label = "Player X"
        self.background_label = "green"
        self.player_count = PLAYER_X_MARKER
        self.player_marker = "X"
        self.already_won = GAME_STATE_RUNNING

    def attach(self, observer):
        """
        Attaches the observer to the observers list

        Parameters
        ----------
        observer : Observer
            The observer which needs to be attached
        Returns
        -------
        """
        self.observers.append(observer)

    def detach(self, observer):
        """
        Detaches the observer from the observers list

        Parameters
        ----------
        observer : Observer
            The observer which needs to be detached

        Returns
        -------
        """
        self.observers.remove(observer)

    def notify(self):
        """
        Notifies the observers to update

        Parameters
        ----------
        Returns
        -------
        None
        """
        for observer in self.observers:
            observer.update()

    def createFile(self):
        """
        Creates new .txt file, which is used to store the game moves

        Parameters
        ----------
        Returns
        -------
        None
        """
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
        open(self.file_name, "a")
        self.history_file()

    def history_file(self):
        """
        Writes game moves to the storage file

        Parameters
        ----------
        Returns
        -------
        None
        """
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
        """
        Returns the line numbers of the given file

        Parameters
        ----------
        file : *.txt
            The chosen *.txt game file

        Returns
        -------
        Returns the total number of lines in the given file
        """
        return sum(1 for _ in open(file))

    def invalid_label(self):
        """
        Notifies the observer for an invalid move

        Parameters
        ----------
        Returns
        -------
        None
        """
        self.state = STATE_NEW_INFO_LABEL
        self.info_label = INVALID_INPUT
        self.notify()

    def valid_label(self):
        """
        Notifies the observer for an valid move

        Parameters
        ----------
        Returns
        -------
        None
        """
        self.state = STATE_NEW_BUFFER
        self.notify()
        self.state = STATE_NEW_INFO_LABEL
        self.info_label = VALID_INPUT
        self.notify()

    def user_choice(self, choice):
        """
        Handles the input of the user

        Parameters
        ----------
        choice : int/str
            The input command of the user

        Returns
        -------
        UNDO: int
            Signals the controller that the user input was UNDO
        REDO: int
            Signals the controller that the user input was REDO
        INVALID: int
            Signals the controller that the user input was INVALID
        NEW_GAME: int
            Signals the controller that the user input was NEW_GAME
        LOAD_GAME: int
            Signals the controller that the user input was LOAD_GAME
        SAVE_GAME: int
            Signals the controller that the user input was SAVE_GAME
        int(choice): int
            Signals the controller which game field the current player picked

        """
        if self.player_count == PLAYER_X_MARKER:
            self.player_marker = "X"
        else:
            self.player_marker = "O"

        acceptable_range = range(1, 10)
        if not choice.isdigit():
            if choice == "U":
                if self.current_line_history == 1:
                    self.invalid_label()
                    return INVALID
                self.undo(False)
                return UNDO
            if choice == "R":
                return INVALID if self.undo(True) == INVALID else REDO
            if choice == "N":
                self.buffer = ["Ä", " ", " ", " ", " ", " ", " ", " ", " ", " "]
                self.player_count = PLAYER_X_MARKER
                self.current_line_history = 0
                self.createFile()
                self.state = STATE_NEW_BUFFER
                self.notify()
                self.state = STATE_CURRENT_PLAYER
                self.current_player_label = f"Player {PLAYER_X_MARKER}"
                self.background_label = "green"
                self.notify()
                return NEW_GAME
            if choice == "L":
                self.player_count = PLAYER_X_MARKER if self.load_game() else PLAYER_O_MARKER
                self.state = STATE_NEW_BUFFER
                self.notify()
                self.state = STATE_CURRENT_PLAYER
                self.current_player_label = f"Player {self.player_count}"
                self.background_label = "green" if self.player_count == PLAYER_X_MARKER else "pink"
                self.notify()
                return LOAD_GAME
            if choice == "S":
                self.save_game()
                return SAVE_GAME
            return INVALID
        elif int(choice) not in acceptable_range:
            return INVALID
        if not self.free_space_check(choice):
            return INVALID

        return int(choice) if self.already_won == GAME_STATE_RUNNING else INVALID

    def load_game(self):
        """
        Used to load an old game
        ----------
        Returns
        -------
        True/False: bool
            If True is returned it is the turn of Player X otherwise the turn of Player O
        """
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
        """
        Used to saved the current game as .txt file
        ----------
        Returns
        -------
        """
        saved_file_name = easygui.filesavebox(filetypes=['*.txt'])

        if saved_file_name[-4:] != ".txt":
            saved_file_name += ".txt"

        try:
            shutil.copyfile(self.file_name, saved_file_name)
        except shutil.SameFileError:
            pass

    def set_marker(self, position, computer):
        """
        Used to update the current game field
        ----------
        position : int
            The chosen position of the current player
        computer : bool
            To signal if it is the turn of the computer
        Returns
        -------
        """
        if position == UNDO or position == REDO:
            return
        self.buffer[position] = PLAYER_O_MARKER if computer else self.player_marker
        self.history_file()
        self.state = STATE_NEW_BUFFER
        self.notify()

    def win_check(self, current_player):
        """
        To check the winning condition of the game
        ----------
        current_player : str
            The current player's marker

        Returns
        -------
        True: bool
            Returns True if the game is over(Win/Draw)
        """
        win_pos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for x in win_pos:
            check = True
            for y in x:
                if self.buffer[y] != current_player:
                    check = False
                    break
            if check:
                self.info_label = "Player " + current_player + " won the Game!"
                self.state = STATE_NEW_INFO_LABEL
                self.notify()
                self.already_won = GAME_STATE_ENDED
                return True
        if " " not in self.buffer:
            self.info_label = "DRAW!"
            self.state = STATE_NEW_INFO_LABEL
            self.notify()
            self.already_won = GAME_STATE_ENDED
            return True
        self.info_label = VALID_INPUT
        self.state = STATE_NEW_INFO_LABEL
        self.notify()
        self.already_won = GAME_STATE_RUNNING

    def free_space_check(self, position):
        """
        To check if the chosen position is empty
        ----------
        position : int
            The chosen position of the current player

        Returns
        -------
        True/False : bool
            Returns True if the chosen position is empty on the game field
        """
        return True if self.buffer[int(position)] == " " else False

    def undo(self, redo):
        """
        To undo and redo the current game moves
        ----------
        redo : bool
            The signal that the user input was "R" (Redo)

        Returns
        -------
        INVALID: int
            Signals the controller that the user input was INVALID
        """
        file_to_game = self.file_name

        if redo:
            self.current_line_history += 1
            if self.get_file_line_numbers(self.file_name) < self.current_line_history:
                self.current_line_history -= 1
                self.invalid_label()
                return INVALID

        else:
            self.current_line_history -= 1
        linecache.clearcache()
        undo_history_line = linecache.getline(file_to_game, self.current_line_history)
        for index, marker in enumerate(undo_history_line):
            if len(self.buffer) != index + 1:
                self.buffer[index + 1] = marker
        self.valid_label()

    def checkIfAlreadyWon(self):
        """
        Checks the win condition for both players
        ----------
        Returns
        -------
        """
        if not self.win_check(PLAYER_X_MARKER):
            self.win_check(PLAYER_O_MARKER)
