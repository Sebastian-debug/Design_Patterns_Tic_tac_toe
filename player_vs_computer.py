from model import *
from random import randint


class PlayerVsComputer():
    """
    A class to implement the behaviour of the player vs computer game mode.

    Attributes
    ----------
    Methods
    -------
    strategy(player_count):
       the function for handling the move of the computer
    """

    def strategy(self, player_count):
        """
         Updates the labels according to the current state of the model
        Parameters
        ----------
        player_count : str
            The current player's marker

        Returns
        -------
        player_count : str
            The current player's marker
        """
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
        model.win_check(PLAYER_O_MARKER)
        return player_count
