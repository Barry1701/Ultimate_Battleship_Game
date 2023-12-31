from random import randint
import json

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
        self.ships = []
    
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

def get_coordinates_from_player():
     try:
        x = int(input("Enter the row where You want to place the ship:"))
        y = int(input("Enter the column where You want to place the ship:"))
        return x, y
     except ValueError:
        print("Invalid Input. Please enter valid numbers(0-4)")
        return None


def valid_coordinates(x, y, ships):
    """
    Check if the given coordinates are valid for the board.
    """
    size = len(ships)
    #check range of coordintates
    if 0 <= x < size and 0 <= y < size:
        #Check availability of the cell
        if ships[x][y] == ".":
            return True
        else:
            print("This cell is already occupied. Choose different one.")
    else:
        print("Coordinates are out of the board range.Choose between 0 & 4.")
        return False

   
    
  


def populate_board(board):
    """
    Add ships to the board randomly.
    """
    num_ships = len(board.ships)
    size = len(board.board)

    while num_ships < board.num_ships:
        x = random_point(size)
        y = random_point(size)
    
        if valid_coordinates(x, y, board.board):
            #add ship on the board
            board.add_ship(x, y)
            num_ships += 1

    


def make_guess(board):
    """
    Generate random coordinates for the computer or prompts player for the input
    """
    if board.type == "computer":
        #Computer guess: pick random coordinates
        x = random_point(board.size)
        y = random_point(board.size)
    else:
        #Player guess: prompt player for input
        coordinates = get_coordinates_from_player()
        while coordinates is None or not valid_coordinates(coordinates[0], coordinates[1], board.board):
            
            coordinates = get_coordinates_from_player()

        x, y = coordinates

    return x, y



def save_scores(scores):
    """
    Safe the scores dictionary to JSON file
    """
    with open("scores.json", "w") as file:
        json.dump(scores, file)
    
def load_scores():
    """
    Load scores from JSON file
    """
    try:
        with open("scores.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return{"computer" : 0, "player" : 0}

def update_scores(winner, scores):
    """
    Update scores dictionary based on the winner of the game
    """
    scores[winner] += 1
    save_scores(scores)

       





def play_game(computer_board, player_board, scores):
    """
    Simulates game of Battleship between Player and Computer
    """
    while True:
        print("\n" + "-" * 48) 
        print("Computer Board:")
        computer_board.print()
        print("\n" + "-" * 48)
        print(f"{player_board.name}'s Board:")
        player_board.print()

        #Player makes a move
        print("\n" + "-" *  48)
        print(f"{player_board.name} Turn:")
        player_guess = make_guess(player_board)
        result = computer_board.guess(*player_guess)
        print(result)

        #Checking the game termination condition
        if all(coords == "*" for row in computer_board.board for coords in row):
            print(f"Congratulations {player_board.name} ! You have won!")
            update_scores("player", scores)
            break

        #Computer makes a move
        print("\n" + "-" * 48)
        print("Computer's Turn:")
        computer_guess = make_guess(computer_board)
        result = player_board.guess(*computer_guess)
        print(result)

        #Checking the game termination condition
        if all(coords == "*" for row in player_board.board for coords in row):
            print("Computer has Won! Better luck next time")
            update_scores("computer", scores)
            break






def new_game():
        """
        Starts a game. Sets the board size and number of ships.
        Resets the scores and initialises the board.
        """                   
        size = 5
        num_ships = 4
        scores = load_scores()
        print("Scores:", scores)
        print("-" * 48)
        print("Welcome to the ULTIMATE BATTLESHIPS")
        print(f"Board Size: {size}. Number Of the Ships: {num_ships}")
        print("Top left corner is Row: 0, Column: 0")
        print("-" * 48)
        player_name = input("Please enter your name: \n")
        print("-" * 48)

        computer_board = Board(size, num_ships, "Computer", type= "computer")
        player_board = Board(size, num_ships, player_name, type= "player")

        for _ in range(num_ships):
            populate_board(player_board)
            populate_board(computer_board)
        
        play_game(computer_board, player_board, scores)


        play_again = input("Do You want to play again? (yes/no):   ").lower()
        if play_again == "yes":
            new_game()
        else:
            print("Thank You for playing!")

new_game()


    
    
