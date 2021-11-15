from constants import *
from model import *

class PlayerVsComputer():
    def __init__(self):
        self.name = "PlayerVsComputer"

    def strategy(self, player_count):
        model = Model.getInstance()
        for position in range(1, 10):
            if model.free_space_check(position):
                model.set_marker(position)
                break
        model.state = STATE_CURRENT_PLAYER
        model.current_player_label = f"Player {player_count}"
        model.background_label = "green"
        model.notify()
        return player_count

