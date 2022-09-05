from game import*

class UI:
    def __init__(self):
        self.game = Game()

    def read_battleships(self, message, nr_of_squares):
        print(message)
        while True:
            try:
                square = input('Enter the origin: >')
                direct = input('Enter the direction (N,S,E,W): >')
                self.game.place_ship(square, direct, nr_of_squares)
                print(self.game.player_board)
                break
            except ValueError as error:
                print(error)

    def read_players_board(self):
        print('Place your ships, master!')
        self.read_battleships('Place your battleship (4 squares)! :)',4)
        self.read_battleships('Place your cruiser (3 squares)! :)',3)
        self.read_battleships('Place your destroyer (2 squares)! :)',2)
    
    def read_users_target(self):
        try:
            square = input('Enter your target: >')
            self.game.users_guess(square)
        except ValueError as error:
            print(error)
            return False

    def run(self):
        print(ui.game.computer_board)
        ui.read_players_board()
        while True:
            if self.read_users_target() != False:
                print(self.game.targeting_board)
                try:
                    self.game.game_won_by_user()
                except GameWonException:
                    print('YES! You have won!!!')
                    break
                self.game.complete_players_board_with_computer_guess()
                print(self.game.player_board)
                try:
                    self.game.game_won_by_computer()
                except GameWonException:
                    print('Oh NO! You have lost! :(')
                    break


