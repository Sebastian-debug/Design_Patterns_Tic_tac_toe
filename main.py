from controller import *
from PlayerVsPlayer import *
from PlayerVsComputer import *
from user_strategy import *

if __name__ == "__main__":
    strategy = PlayerVsPlayer()
    c = Controller(strategy)
