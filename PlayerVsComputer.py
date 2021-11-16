from constants import *
from model import *
from random import randint

class PlayerVsComputer():
    def __init__(self):
        self.name = "PlayerVsComputer"

    def strategy(self, player_count):
        model = Model.getInstance()
        position = randint(1, 9)
        values = set()
        possible_positions = [x for x in range(1, 10)]
        while not model.free_space_check(position):
            position = randint(1, 9)
            values.add(position)
            if values == set(possible_positions):
                break
        model.set_marker(position, True)

        model.state = STATE_CURRENT_PLAYER
        model.current_player_label = f"Player {player_count}"
        model.background_label = "green"
        model.notify()
        return player_count

