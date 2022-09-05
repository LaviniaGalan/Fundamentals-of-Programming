import tkinter as tk
from tkinter import messagebox
from game import*

class GUI:
    def __init__(self):
        self.game = Game()
        self.window = tk.Tk()
        self.window.geometry('1536x800')
        self.run_1st_part()
        self.nr_of_ships = 0

    def run_1st_part(self):
        # 1st part = the beginning of the game, when the user places his ship
        frame1 = tk.Frame(self.window, bg='#ffe6cc')
        frame1.place(relx=0.15, rely=0.1, relwidth=0.3, relheight=0.6)
        label = tk.Label(frame1, text = 'Your board', font = 28, bg = '#ffe6cc')
        label.place(relx=0.38, rely = 0.05)
        subframe1 = tk.Frame(frame1, bg='#ffe6cc')
        subframe1.place(relx = 0.18, rely = 0.15, relwidth = 0.66, relheight = 0.7)
        for row in range(8):
            for col in range(8):
                button = tk.Button(subframe1, text = " ", width = 4, height = 2, bg = 'white', command = lambda row = row, col = col: self.chosen_ship(subframe1, row, col))
                button.grid(row = row, column = col)

    def chosen_ship(self, subframe1, row, col):
        if self.nr_of_ships >= 3:
            messagebox.showerror("Error", "Gata cu construitul de nave!!")
            return
        direct_window = tk.Tk()
        direct_window.grab_set()
        directions = ['N', 'S', 'E', 'W']
        for i in directions:
            button = tk.Button(direct_window, text = i, width= 4, height = 2, bg = 'white', command = lambda i = i:self.place_ship(subframe1, row, col, i, 4-self.nr_of_ships, direct_window))
            button.pack()

    def place_ship(self, subframe1, row, col, direct, nr_of_squares, window):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        try:
            if self.nr_of_ships < 3:
                row = row + 1
                square = str(row) + ' ' + letters[col]
                self.nr_of_ships += 1
                squares_taken = self.game.place_ship(square, direct, nr_of_squares)
                for j in squares_taken:
                    label = tk.Label(subframe1, text="□", width=4, height=2, bg='#ff8c1a')
                    label.grid(row = j[0], column = j[1])
            else:
                messagebox.showerror("Error", "Gata cu construitul de nave!!")
        except  ValueError as error:
            messagebox.showerror("Error", error)
            self.nr_of_ships -= 1
        window.grab_release()
        window.destroy()
        if self.nr_of_ships == 3:
            self.run_2nd_part(subframe1)

    def run_2nd_part(self, subframe1):
        # 2nd part = the rest of the game, when the players try to 'attack' the opponent's ships
        frame2 = tk.Frame(self.window, bg='#ffe6cc')
        frame2.place(relx=0.55, rely=0.1, relwidth=0.3, relheight=0.6)
        label = tk.Label(frame2, text='Your targeting board', font=28, bg='#ffe6cc')
        label.place(relx=0.3, rely=0.05)
        subframe2 = tk.Frame(frame2, bg='#ffe6cc')
        subframe2.place(relx=0.18, rely=0.15, relwidth=0.66, relheight=0.7)
        for row in range(8):
            for col in range(8):
                button = tk.Button(subframe2, text=" ", width=4, height=2, bg='white',
                                   command=lambda row=row, col=col: self.users_guess(subframe1, subframe2, row, col))
                button.grid(row = row, column = col)

    def users_guess(self, subframe1, subframe2, row, col):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        try:
            row = row + 1
            square = str(row) + ' ' + letters[col]
            symbol = self.game.users_guess(square)
            label = tk.Label(subframe2, text=symbol, width=4, height=2, bg='#ff471a')
            label.grid(row = row-1, column = col)
        except Exception as error:
            messagebox.showerror("Error", error)
            return
        try:
            self.game.game_won_by_user()
        except GameWonException:
            messagebox.showinfo("Game won!", "Congrats! you have won!")
            self.window.after(700, lambda: self.window.destroy())
            return
        self.computers_guess(subframe1)
        try:
            self.game.game_won_by_computer()
        except GameWonException:
            messagebox.showinfo("Game lost!", "OOH NO! You have lost! :(")
            self.window.after(700, lambda: self.window.destroy())
            return

    def computers_guess(self, subframe1):
        pair  = self.game.complete_players_board_with_computer_guess()
        coord = pair[0]
        symbol = pair[1]
        label = tk.Label(subframe1, text=symbol, width=4, height=2, bg='#ff471a')
        label.grid(row = coord[0], column = coord[1])

gui = GUI()
gui.window.mainloop()