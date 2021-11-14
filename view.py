from tkinter import *

class View(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.player_1_marker = "X"
        self.player_2_marker = "O"
        self.label_marker_list = list()

        self.title('TicTacToe')
        self.geometry("800x800")
        self.configure(bg="black")
        self.resizable(0, 0)

        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=3)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=3)
        self.rowconfigure(2, weight=3)
        self.cross_photo = PhotoImage(file='Cross3.png')
        self.circle_photo = PhotoImage(file='circle.png')
        self.blank_photo = PhotoImage(file='blank.png')

        self.label1 = Label(master=self, bg='white', text="7", height=15, width=36, anchor=SE,
                       font=('Helvetica', 9, 'bold'))
        self.label1.grid(row=0, column=0)

        self.label1_marker = Label(master=self, image=self.blank_photo)
        self.label1_marker.grid(row=0, column=0)

        self.label2 = Label(master=self, bg='white', text="4", height=16, width=36, anchor=SE,
                       font=('Helvetica', 9, 'bold'))
        self.label2.grid(row=1, column=0)

        self.label2_marker = Label(master=self, image=self.blank_photo)
        self.label2_marker.grid(row=1, column=0)

        self.label3 = Label(master=self, bg='white', text="1", height=16, width=36, anchor=SE,
                       font=('Helvetica', 9, 'bold'))
        self.label3.grid(row=2, column=0)

        self.label3_marker = Label(master=self, image=self.blank_photo)
        self.label3_marker.grid(row=2, column=0)

        self.label4 = Label(master=self, bg='white', text="8", height=15, width=36, anchor=SE,
                       font=('Helvetica', 9, 'bold'))
        self.label4.grid(row=0, column=1)

        self.label4_marker = Label(master=self, image=self.blank_photo)
        self.label4_marker.grid(row=0, column=1)

        self.label5 = Label(master=self, bg='White', text="5", height=16, width=36, anchor=SE,
                       font=('Helvetica', 9, 'bold'))
        self.label5.grid(row=1, column=1)

        self.label5_marker = Label(master=self, image=self.blank_photo)
        self.label5_marker.grid(row=1, column=1)

        self.label6 = Label(master=self, bg='White', text="2", height=16, width=36, anchor=SE,
                       font=('Helvetica', 9, 'bold'))
        self.label6.grid(row=2, column=1)

        self.label6_marker = Label(master=self, image=self.blank_photo)
        self.label6_marker.grid(row=2, column=1)

        self.label7 = Label(master=self, bg='White', text="9", height=15, width=36, anchor=SE,
                       font=('Helvetica', 9, 'bold'))
        self.label7.grid(row=0, column=2)

        self.label7_marker = Label(master=self, image=self.blank_photo)
        self.label7_marker.grid(row=0, column=2)

        self.label8 = Label(master=self, bg='White', text="6", height=16, width=36, anchor=SE,
                       font=('Helvetica', 9, 'bold'))
        self.label8.grid(row=1, column=2)

        self.label8_marker = Label(master=self, image=self.blank_photo)
        self.label8_marker.grid(row=1, column=2)

        self.label9 = Label(master=self, bg='White', text="3", height=16, width=36, anchor=SE,
                       font=('Helvetica', 9, 'bold'))
        self.label9.grid(row=2, column=2)

        self.label9_marker = Label(master=self, image=self.blank_photo)
        self.label9_marker.grid(row=2, column=2)

        self.label10 = Label(master=self, bg='#FF0000', text="[1-9] Pick [U] Undo [R] Redo [N] New\n  [L] Load [S] Save",
                        width=30,
                        anchor=CENTER,
                        font=('Helvetica', 8, 'bold'))
        self.label10.grid(row=4, column=1)

        self.label11 = Label(master=self, bg='green', text="Player X", width=20, anchor=CENTER,
                        font=('Helvetica', 9, 'bold'))
        self.label11.grid(row=4, column=2)

        self.entry1 = Entry(master=self, bg='#FFFFFF', width="40")
        self.entry1.grid(row=5, column=1, padx='5', pady='5')

        self.label_marker_list.append(self.label3_marker)
        self.label_marker_list.append(self.label6_marker)
        self.label_marker_list.append(self.label9_marker)
        self.label_marker_list.append(self.label2_marker)
        self.label_marker_list.append(self.label5_marker)
        self.label_marker_list.append(self.label8_marker)
        self.label_marker_list.append(self.label1_marker)
        self.label_marker_list.append(self.label4_marker)
        self.label_marker_list.append(self.label7_marker)

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
            if field == "O":
                self.label_marker_list[index]['image'] = self.circle_photo
            if field == " ":
                self.label_marker_list[index]['image'] = self.blank_photo
