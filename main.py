import random
import easygui
import linecache
import os
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
    line_numbers = sum(1 for _ in open("history.txt"))

    with open('history.txt', "a+") as file:
        if current_line_history != line_numbers:
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
        line_numbers = sum(1 for _ in open("history.txt"))
        current_line_history += 1
        if line_numbers < current_line_history:
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
