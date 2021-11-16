from model import *


class PlayerVsPlayer:
    """
    A class to implement the behaviour of the player vs player game mode.

    Attributes
    ----------
    Methods
    -------
    strategy(player_count):
       the function for handling the switch between players
    """

    def strategy(self, player_count):
        """
        Updates the markers of the players according to the current turn
        Parameters
        ----------
        player_count : str
            The current player's marker

        Returns
        -------
        PLAYER_O_MARKER : str
            The marker of the O player
        PLAYER_X_MARKER : str
            The marker of the X player
        """
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
