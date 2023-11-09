from random import randint

scores = {"computer": 0, "player": 0 }

class Board:
    """
    Main board class. Sets board size, the number of ships,
    the player's name and the board type(player board or computer)
    has menthods for adding ships, guesses and printing the board.
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ship = num_ship
        self.name = name
        self.type = type
        self.guesses = []
        self.ship = []