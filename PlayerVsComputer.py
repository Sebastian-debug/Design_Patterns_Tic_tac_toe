from constants import *
from model import *

class PlayerVsComputer(object):
    def __init__(self):
        self.name = "PlayerVsComputer"

    def strategy(self, player_count):
        model = Model.getInstance()
        for position in range(1, 10):
            if model.free_space_check(position):
                model.set_marker(PLAYER_O_MARKER, position)
                break
        return player_count, f"Player {player_count}", "green"

