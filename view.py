from tkinter import *


class View(Tk):
    singleton_instance = None

    @staticmethod
    def getInstance():
        if View.singleton_instance is None:
            return View()
        else:
            return View.singleton_instance

    def __init__(self):
        if View.singleton_instance is not None:
            raise Exception("There can only be one instance of View")
        else:
            View.singleton_instance = self
        Tk.__init__(self)
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
                                 text="[1-9] Pick [U] Undo [R] Redo [N] New\n  [L] Load [S] Save", width=30,
                                 anchor=CENTER,
                                 font=('Helvetica', 8, 'bold'))
        self.label_start.grid(row=4, column=1)
        self.label_players = Label(master=self, bg='green', text="Player X", width=20, anchor=CENTER,
                                   font=('Helvetica', 9, 'bold'))
        self.label_players.grid(row=4, column=2)
        self.user_entry = Entry(master=self, bg='#FFFFFF', width="40")
        self.user_entry.grid(row=5, column=1, padx='5', pady='5')

    def display(self, buffer, current_line_history):
        print("\n" * 100)
        print(f"      |      "  "  |\n"
              f" {buffer[7]}    |   {buffer[8]}  "f"  |  {buffer[9]}\n"
              "      |      "  "  |\n"
              "--------------------")
        print(f"      |      "  "  |\n"
              f" {buffer[4]}    |   {buffer[5]}  "f"  |  {buffer[6]}\n"
              "      |      "  "  |\n"
              "--------------------")
        print(f"      |      "  "  |\n"
              f" {buffer[1]}    |   {buffer[2]}  "f"  |  {buffer[3]}\n"
              "      |      "  "  |\n")

        print(f"current_line_history: {current_line_history}\n")
        for index, field in enumerate(buffer[1:]):
            print("Field: " + field + " Index: " + str(index))
            if field == "X":
                self.label_marker_list[index]['image'] = self.cross_photo
            elif field == "O":
                self.label_marker_list[index]['image'] = self.circle_photo
            else:
                self.label_marker_list[index]['image'] = self.blank_photo
