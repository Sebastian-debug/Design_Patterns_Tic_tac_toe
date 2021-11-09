import random
import easygui
import linecache
import os
from tkinter import *
from math import inf


buffer = ["Ä", " ", " ", " ", " ", " ", " ", " ", " ", " "]
current_line_history = 0


def display():
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


def user_choice(player):
    choice = 'WRONG'
    acceptable_range = range(1, 10)
    within_range = False
    while not within_range:
        if current_line_history > 1:
            print("You can use the command 'U' to undo a game step and 'R' to redo a game step \n")
        choice = input(f"Please Player {player} enter a number between 1 and 9:")

        if not choice.isdigit():
            if choice == "U":
                if current_line_history == 1:
                    print("Sorry, you cannot undo because there are no game steps")
                    continue
                undo(False)
                return 0
            if choice == "R":
                undo(True)
                return 0
            print("Sorry, that is not a valid command!")
            continue
        elif int(choice) not in acceptable_range:
            print("Sorry, you are out of acceptable range (1-9)")
            continue
        if not free_space_check(choice):
            print("Sorry, this position is already taken!")
            continue
        within_range = True
    return int(choice)


def set_marker(marker, position):
    if position == 0:
        return
    buffer[position] = marker
    history_file()


def win_check(mark, player_, computer=False):
    win_pos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for x in win_pos:
        check = True
        for y in x:
            if buffer[y] != mark:
                check = False
                break
        if check:
            if not computer:
                display()
                print(f"Player {player_} won the Game!")
            return True
    if " " not in buffer:
        if not computer:
            display()
            print("DRAW!")
        return True
    return False


def choose_first():
    player_1 = random.randint(1, 2)
    print(f"Player {player_1} starts the game!")
    while True:
        player_1_marker = input(f"Please Player {player_1} select X or O!")
        if player_1_marker != "X" and player_1_marker != "O":
            print("Sorry, that was not X nor O!")
            continue
        else:
            break
    player_2_marker = "X" if player_1_marker == "O" else "O"
    player_2 = 2 if player_1 == 1 else 1
    return {"player_1_marker": player_1_marker, "player_1": player_1,
            "player_2_marker": player_2_marker, "player_2": player_2}


def free_space_check(position):
    return True if buffer[int(position)] == " " else False


def get_file_line_numbers(file):
    return sum(1 for _ in open(file))


def replay():
    while True:
        x = input("Do you want to play again? (Yes/No)").lower()
        if x != "yes" and x != "no":
            continue
        else:
            break
    if x == "yes":
        for x in range(1, 10):
            buffer[x] = " "
        if os.path.exists("history.txt"):
            os.remove("history.txt")
        return True
    return False


def history_file():
    global current_line_history

    with open('history.txt', "a+") as file:
        if current_line_history != get_file_line_numbers("history.txt"):
            file.seek(0)
            tmp_history_lines = file.readlines()
            file.seek(0)
            file.truncate()
            for line in tmp_history_lines[:current_line_history]:
                file.write(line)

        for field in buffer[1:]:
            if field == " ":
                file.write(" ")
            elif field == "X":
                file.write("X")
            else:
                file.write("O")
        file.write("\n")

    current_line_history += 1


def undo(redo):
    file_to_game = "history.txt"
    global current_line_history

    if redo:
        current_line_history += 1
        if get_file_line_numbers("history.txt") < current_line_history:
            current_line_history -= 1
            print("Cannot redo, there are no steps ahead!")
            return
    else:
        current_line_history -= 1

    linecache.clearcache()
    undo_history_line = linecache.getline(file_to_game, current_line_history)

    for index, marker in enumerate(undo_history_line):
        if len(buffer) != index + 1:
            buffer[index + 1] = marker


if __name__ == "__main__":

    tkwindow = Tk()
    tkwindow.title('TicTacToe')
    tkwindow.geometry("800x800")
    tkwindow.configure(bg="black")
    tkwindow.resizable(0,0)

    tkwindow.columnconfigure(0, weight=3)
    tkwindow.columnconfigure(1, weight=3)
    tkwindow.columnconfigure(2, weight=3)
    tkwindow.rowconfigure(0, weight=3)
    tkwindow.rowconfigure(1, weight=3)
    tkwindow.rowconfigure(2, weight=3)
    cross_photo = PhotoImage(file='Cross3.png')
    circle_photo = PhotoImage(file='circle.png')

    label1 = Label(master=tkwindow, bg='white', text="7", height=15, width=36, anchor=SE, font=('Helvetica', 9, 'bold'))
    label1.grid(row=0, column=0)

    label2 = Label(master=tkwindow, bg='white', text="4", height=16, width=36, anchor=SE, font=('Helvetica', 9, 'bold'))
    label2.grid(row=1, column=0)

    label2_marker = Label(master=tkwindow, image=cross_photo)
    label2_marker.grid(row=1, column=0)

    label3 = Label(master=tkwindow, bg='white', text="1", height=16, width=36, anchor=SE, font=('Helvetica', 9, 'bold'))
    label3.grid(row=2, column=0)

    label3_marker = Label(master=tkwindow, image=circle_photo)
    label3_marker.grid(row=2, column=0)

    label4 = Label(master=tkwindow, bg='white', text="8", height=15, width=36, anchor=SE, font=('Helvetica', 9, 'bold'))
    label4.grid(row=0, column=1)

    label5 = Label(master=tkwindow, bg='White', text="5", height=16, width=36, anchor=SE, font=('Helvetica', 9, 'bold'))
    label5.grid(row=1, column=1)

    label6 = Label(master=tkwindow, bg='White', text="2", height=16, width=36, anchor=SE, font=('Helvetica', 9, 'bold'))
    label6.grid(row=2, column=1)

    label7 = Label(master=tkwindow, bg='White', text="9", height=15, width=36, anchor=SE, font=('Helvetica', 9, 'bold'))
    label7.grid(row=0, column=2)

    label8 = Label(master=tkwindow, bg='White', text="6", height=16, width=36, anchor=SE, font=('Helvetica', 9, 'bold'))
    label8.grid(row=1, column=2)

    label9 = Label(master=tkwindow, bg='White', text="3", height=16, width=36, anchor=SE, font=('Helvetica', 9, 'bold'))
    label9.grid(row=2, column=2)

    label10 = Label(master=tkwindow, bg='#FF0000', text="Welcome to TIC TAC TOE :)",  width=30, anchor= CENTER, font=('Helvetica', 9, 'bold'))
    label10.grid(row=3, column=1)

    entry1 = Entry(master=tkwindow, bg='#FFFFFF', width="40")
    entry1.grid(row=4, column=1, padx='5', pady='5')

    tkwindow.mainloop()


    # file = easygui.fileopenbox()
    # print(file) // load game
    if os.path.exists("history.txt"):
        os.remove("history.txt")
    open('history.txt', "a")

    print("Welcome to Tic Tac Toe!")
    history_file()
    while True:
        display()
        player_dict = choose_first()
        while True:
            set_marker(player_dict["player_1_marker"], user_choice(player_dict["player_1"]))
            display()

            if win_check(player_dict["player_1_marker"], player_dict["player_1"]):
                break

            set_marker(player_dict["player_2_marker"], user_choice(player_dict["player_2"]))

            display()
            if win_check(player_dict["player_2_marker"], player_dict["player_2"]):
                break
        if not replay():
            break
