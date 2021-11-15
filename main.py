from controller import *
from PlayerVsPlayer import *
from PlayerVsComputer import *

if __name__ == "__main__":
    strategy = PlayerVsComputer()
    c = Controller(strategy)
