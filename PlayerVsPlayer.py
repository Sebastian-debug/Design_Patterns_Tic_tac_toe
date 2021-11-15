from constants import *


class PlayerVsPlayer:

    def strategy(self, player_count):
        if player_count == PLAYER_X_MARKER:
            return PLAYER_O_MARKER, f"Player {PLAYER_O_MARKER}", "pink"
        else:
            return PLAYER_X_MARKER, f"Player {PLAYER_X_MARKER}", "green"
