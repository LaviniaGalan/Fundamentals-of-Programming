from domain import *
import random

class ComputerGame:
    def __init__(self):
        self.computer_board = Board()
        self.generate_board()

    def generate_board(self):
        '''
        Generates the computer's board.
        '''
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        digits = range(1, 9)
        directions = ['N', 'S', 'E', 'W']
        nr_of_squares = 4
        while nr_of_squares >= 2:
            letter = random.choice(letters)
            col = letters.index(letter) 
            row = random.choice(digits)
            direct = random.choice(directions)
            try:
                self.computer_board.valid_ship(row-1, col, direct, nr_of_squares)
            except ValueError:
                continue
            self.computer_board.place_ship(row-1, col, direct, nr_of_squares)
            nr_of_squares = nr_of_squares - 1

    def computers_guess_random(self):
        '''
        Generates randomly a square which will be the 'target' of the computer.
        output: > col = the column corresponding to the square
                > row = the row corresponding to the square
        '''
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        digits = range(1, 9)
        col = random.choice(letters)
        row = random.choice(digits)
        return(row, col)

        
class Game:
    def __init__(self):
        self.computer = ComputerGame()
        self.computer_board = self.computer.computer_board
        self.player_board = Board()
        self.targeting_board = Board()

    def generate_int_coord(self, square):
        '''
        Transforms the coordinates of the form (digit letter) into the corresponding indexes of the data list.
        params: > square = the square
        output: > returns a pair (x, y) where x and y are the indexes in the data list corresponding to the given square
        '''
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        return (int(square[0])-1, letters.index(square[1]))

    def place_ship(self, square, direct, nr_of_squares):
        '''
        Places a ship on the board, having the origin on the given square and a given direction.
        params: > square = the origin square
                > direction = the direction of the ship w.r.t. the given square
                > nr_of_squares = the number of squares of the ship
        output: > raise Error if the ship can not be placed
                > the list of the occupied squares otherwise.
        '''
        square = square.split(' ')
        if len(square) != 2:
            raise ValueError('Invalid coordinates!')
        if direct not in ['N', 'S', 'E', 'W']:
            raise ValueError('Invalid direction!')
        if self.player_board.valid_coord(square[0], square[1]) is None:
            if self.player_board.empty_square(square[0], square[1], '□') is None:
                coords = self.generate_int_coord(square)
                row = coords[0]
                col = coords[1]
                if self.player_board.valid_ship(row, col, direct, nr_of_squares) is None:
                    squares_taken = self.player_board.place_ship(row, col, direct, nr_of_squares)
        return squares_taken

    def users_guess(self, square):
        '''
        Analyze the 'target' of the user and complete its targeting board respectively.
        params: > square = the square to be analyzed
        output: > raise Error if the square is not valid or if it was already analyzed
                > returns the symbol placed on the board otherwise
        '''
        square = square.split(' ')
        if len(square) != 2:
            raise ValueError('Invalid coordinates!')
        if self.targeting_board.valid_coord(square[0], square[1]) is None:
            if self.targeting_board.empty_square(square[0], square[1], 'X') is None:
                if self.targeting_board.empty_square(square[0], square[1], '✓') is None:
                    coord = self.generate_int_coord(square)
                    if self.computer_board.hit_or_missed(coord[0], coord[1]) is True:
                        self.targeting_board.place_square(coord[0], coord[1], '✓')
                        return '✓'
                    else:
                        self.targeting_board.place_square(coord[0], coord[1], 'X')
                        return 'X'

    def complete_players_board_with_computer_guess(self):
        '''
        Places the computer's guesses on the player's board:
                - '✓' if the computer guessed a square which is part of a player's ship
                - 'X' otherwise.
        output: > returns the coordinates of the checked square and the corresponding symbol.
        '''
        while True:
            guess = self.computer.computers_guess_random()
            try:
                self.player_board.empty_square(str(guess[0]), guess[1], '✓')
                self.player_board.empty_square(str(guess[0]), guess[1], 'X')
                break
            except ValueError:
                continue
        coord = self.generate_int_coord((str(guess[0]), guess[1]))
        if self.player_board.hit_or_missed(coord[0], coord[1]) is True:
            self.player_board.place_square(coord[0], coord[1], '✓')
            symbol = '✓'
        else:
            self.player_board.place_square(coord[0], coord[1], 'X')
            symbol = 'X'
        return (coord, symbol)

    def game_won_by_user(self):
        self.targeting_board.game_won()
    def game_won_by_computer(self):
        self.player_board.game_won()


