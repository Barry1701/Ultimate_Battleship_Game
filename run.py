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
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ship = []
    
    def print(self):
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if(x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"     

    def add_ship(self, x, y, type ="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: You cannot add any more ships")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board [x][y] = "@"

def random_point(size):
        """
        Helper function to return random integer between o and size
        """
        return randint(0, size - 1)

def valid_coordinates(x, y, board):
    """
    Check if the given coordinates are valid for the board.
    """
    size = len(board)
    #check range of coordintates
    if 0 <= x < size and 0 <= y < size:
        #Check availability of the cell
        if board[x][y] == ".":
            return True
        else:
            print("This cell is already oocupied. Choose different one")
    else:
        print("Coordinates are out of the board range.Choose between 0 & 4")
        return False

    



def populate_board(board)


def make_guess(board)


def play_game(computer_board, player_board)


def new_game():
        """
        Starts a game. Sets the board size and number of ships.
        Resets the scores and initialises the board.
        """                   
        size = 5
        num_ships = 4
        scores["computer"] = 0
        scores["player"] = 0
        print("-" * 38)
        print("Welcome to the ULTIMATE BATTLESHIPS")
        print(f"Board Size: {size}. Number Of the Ships: {num_ships}")
        print("Top left corner is Row: 0, Column: 0")
        print("-" * 38)
        player_name = input("Please enter your name: \n")
        print("-" * 38)

        computer_board = Board(size, num_ships, "Computer", type= "computer")
        player_board = Board(size, num_ships, player_name, type= "player")

        for _ in range(num_ships):
            populate_board(player_board)
            populate_board(computer_board)
        
        play_game(computer_board, player_board)

new_game()


    
    
