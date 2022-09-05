from texttable import Texttable

class GameWonException(Exception):
    pass

class Board:
    def __init__(self):
        self.data = [[0]*8,
                    [0]*8,
                    [0]*8,
                    [0]*8,
                    [0]*8,
                    [0]*8,
                    [0]*8,
                    [0]*8]

    def game_won(self):
        '''
        If one of the players won, raises an exception.
        '''
        total = 0
        for row in self.data:
            for j in row:
                if j == 1:
                    total = total + 1
        if total == 9:
            raise GameWonException 

    def valid_coord(self, x, y):
        '''
        Chceks if the coordinates introduced by user are valid.
        params: > x = the digit corresponding to the row
                > y = the letter corresponding to the column
        output: > raise Value Error if the coordinates are invalid
                > return None otherwise.
        '''
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        if y not in letters or x.isdigit() is False or int(x) not in range(1,9):
            raise ValueError('Invalid coordinates!')
        
    def empty_square(self, x, y, symbol):
        '''
        Checks if the square having the coordinates (x, y) does not contain the mentioned symbol.
        params: > x = the digit corresponding to the row
                > y = the letter corresponding to the column
                > symbol = the symbol to be checked
        output: > raise Value Error if the square already has that symbol
                > return None otherwise.
        '''
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        # overlapping battleship:
        if symbol == '□' and self.data[int(x)-1][letters.index(y)] == 2:
            raise ValueError('Already a battleship here!')
        # the square was already checked:
        if symbol in ['✓', 'X'] and self.data[int(x)-1][letters.index(y)] in [-1, 1]:
            raise ValueError('Square already checked!')

    def place_square(self, x, y, symbol):
        '''
        Places a symbol on a square.
        params: > x = the digit corresponding to the row (the index in the data list)
                > y = the digit corresponding to the column (the index in the data list)
        '''
        d = {0:' ', -1:'X', 1:'✓', 2:'□'}
        self.data[x][y] = list(d.keys())[list(d.values()).index(symbol)]
    
    def valid_ship(self, row, col, direct, nr_of_squares):
        '''
        Checks if a ship introduced by user is valid.
        params: > row = the digit corresponding to the row of the origin square (the index in the data list)
                > col = the digit corresponding to the column of the origin square (the index in the data list)
                > direct = the direction of the ship w.r.t. the origin square
                > nr_of_squares = the numbers of squares occupied by the ship
        output: > raise Value Error if the ship is not valid
                > return None otherwise.
        '''
        directions = {'N':[-1, 0], 'S':[1, 0], 'E':[0, 1], 'W':[0, -1]}
        if row + directions[direct][0]*nr_of_squares < 0 or row + directions[direct][0]*nr_of_squares > 8 or col + directions[direct][1]*nr_of_squares < 0 or col + directions[direct][1]*nr_of_squares>8:
            raise ValueError('Ship outside the board!')
        for i in range(0, nr_of_squares):
            if self.data[row][col] == 2:
                raise ValueError('The ship overlaps with other!')
            row = row + directions[direct][0]
            col = col + directions[direct][1]

    def place_ship(self, row, col, direct, nr_of_squares):
        '''
        Places a ship introduced by the user.
        params: > row = the digit corresponding to the row of the origin square (the index in the data list)
                > col = the digit corresponding to the column of the origin square (the index in the data list)
                > direct = the direction of the ship w.r.t. the origin square
                > nr_of_squares = the numbers of squares occupied by the ship
        output: > returns a list with the pairs which are the coordinates of the occupied squares
        '''
        squares_taken = []
        directions = {'N':[-1,0],'S':[1,0],'E':[0,1],'W':[0,-1]}
        for i in range(0, nr_of_squares):
            self.data[row][col] = 2
            squares_taken.append((row, col))
            row = row + directions[direct][0]
            col = col + directions[direct][1]
        return squares_taken


    def hit_or_missed(self, x, y):
        '''
        Checks if a given square is part of a ship.
        params: > x = the digit corresponding to the row of the square (the index in the data list)
                > y = the digit corresponding to the column of the square (the index in the data list)
        output: > return True if the square is part of a ship
                > return False otherwise.
        '''
        if self.data[x][y] == 2:
            return True
        else:
            return False

    def get_square(self, x, y):
        '''
        Returns the value of a given square.
        params: > x = the digit corresponding to the row of the square (the index in the data list)
                > y = the digit corresponding to the column of the square (the index in the data list)
        output: > the value of the square having coordinates (x, y)
        '''
        return self.data[x][y]

    def __str__(self):
        # 0 - nothing
        # -1 - missed
        # 1 - hit
        # 2 - original battleship
        t = Texttable()
        d = {0:' ', -1:'X', 1:'✓', 2:'□'}
        row = ['0','A','B','C','D','E','F','G','H']
        t.add_row(row)
        for i in range(8):
            row = [i+1]
            row.extend(self.data[i][:])
            for j in range(1,9):
                row[j] = d[row[j]]
            t.add_row(row)
        return t.draw()

