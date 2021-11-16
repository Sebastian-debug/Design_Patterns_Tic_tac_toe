from tkinter import *
from observer import *
from constants import *


class View(Tk, Observer):
    """
    A class to represent the View.

    Attributes
    ----------
    model : Model
        the model instance

    Methods
    -------
    update():
        Updates the labels according to the current state of the model
    """
    def __init__(self, model):
        """
        Parameters
        ----------
        model: Model
            the model instance

        """
        Tk.__init__(self)
        self.model = model
        self.model.attach(self)
        self.player_1_marker = "X"
        self.player_2_marker = "O"
        self.label_marker_list = list()
        self.title('TicTacToe')
        self.geometry("800x800")
        self.configure(bg="black")
        self.resizable(0, 0)
        for counter_config in range(4):
            self.columnconfigure(counter_config, weight=3)
            self.rowconfigure(counter_config, weight=3)
        self.cross_photo = PhotoImage(file='Cross3.png')
        self.circle_photo = PhotoImage(file='circle.png')
        self.blank_photo = PhotoImage(file='blank.png')

        list_markers_tuples = [(2, 0), (2, 1), (2, 2), (1, 0), (1, 1), (1, 2), (0, 0), (0, 1), (0, 2)]
        switch_row_counter, text_counter = 0, 1
        for row_col_tuple in list_markers_tuples:
            Label(master=self, bg='white', text=f"{text_counter}", height=15, width=36, anchor=SE,
                  font=('Helvetica', 9, 'bold')).grid(row=row_col_tuple[0], column=row_col_tuple[1])
            text_counter += 1
            label_marker = Label(master=self, image=self.blank_photo)
            label_marker.grid(row=row_col_tuple[0], column=row_col_tuple[1])
            self.label_marker_list.append(label_marker)

        self.label_start = Label(master=self, bg='#FF0000',
                                 text=VALID_INPUT, width=30,
                                 anchor=CENTER,
                                 font=('Helvetica', 8, 'bold'))
        self.label_start.grid(row=4, column=1)
        self.label_players = Label(master=self, bg='green', text="Player X", width=20, anchor=CENTER,
                                   font=('Helvetica', 9, 'bold'))
        self.label_players.grid(row=4, column=2)
        self.user_entry = Entry(master=self, bg='#FFFFFF', width="40")
        self.user_entry.grid(row=5, column=1, padx='5', pady='5')

    def update(self):
        """
         Updates the labels according to the current state of the model
        Parameters
        ----------
        Returns
        -------
        None
        """
        if self.model.state == STATE_NEW_BUFFER:
            for index, field in enumerate(self.model.buffer[1:]):
                if field == "X":
                    self.label_marker_list[index]['image'] = self.cross_photo
                elif field == "O":
                    self.label_marker_list[index]['image'] = self.circle_photo
                else:
                    self.label_marker_list[index]['image'] = self.blank_photo
        elif self.model.state == STATE_NEW_INFO_LABEL:
            self.label_start["text"] = self.model.info_label
            if self.model.info_label == INVALID_INPUT:
                return
        elif self.model.state == STATE_CURRENT_PLAYER:
            self.label_players["text"] = self.model.current_player_label
            self.label_players["bg"] = self.model.background_label

        self.user_entry.delete(0, END)
