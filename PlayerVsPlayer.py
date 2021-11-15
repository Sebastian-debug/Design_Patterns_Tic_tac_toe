from constants import *
from model import *

class PlayerVsPlayer:

    def strategy(self, player_count):
        model = Model.getInstance()
        if player_count == PLAYER_X_MARKER:
            model.state = STATE_CURRENT_PLAYER
            model.current_player_label = f"Player {PLAYER_O_MARKER}"
            model.background_label = "pink"
            model.notify()
            return PLAYER_O_MARKER
        else:
            model.state = STATE_CURRENT_PLAYER
            model.current_player_label = f"Player {PLAYER_X_MARKER}"
            model.background_label = "green"
            model.notify()
            return PLAYER_X_MARKER
