class TicTacToe:

    def __init__(self):
        self.player = "X"
        self.x_count = 0
        self.o_count = 0
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.win = False
        self.str = 0
        self.case = 0
        self.cords = [13, 23, 33, 12, 22, 32, 11, 21, 31]
        self.cords_d = {k: v for v, k  in enumerate(self.cords)}

    def drawing_field(self):
        field = ("---------\n"
                 f"| {self.cells[0]} {self.cells[1]} {self.cells[2]} |\n"
                 f"| {self.cells[3]} {self.cells[4]} {self.cells[5]} |\n"
                 f"| {self.cells[6]} {self.cells[7]} {self.cells[8]} |\n"
                 "---------")
        return field

    def player_turn(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

    def players_input(self):
        while True:
            x = "".join(input("Enter the coordinates: ")).split()
            for i in x:
                try:
                    if int(i) > 3:
                        print("Coordinates should be from 1 to 3!")
                        break
                    elif len(x) != 2:
                        print("Please enter two digit coordinates")
                        break
                except ValueError:
                    print("You should enter numbers!")
                    break
            else:
                user_cords = int("".join(x))
                if self.cells[self.cords_d[user_cords]] != "X" and self.cells[self.cords_d[user_cords]] != "O":
                    self.cells[self.cords_d[user_cords]] = self.player
                    self.player_turn()
                    print(self.drawing_field())
                    break
                else:
                    print("This cell is occupied! Choose another one!")

    def win_test(self):
        self.str = ("".join(self.cells))
        self.case = [self.str[0:3], self.str[3:6], self.str[6:9], self.str[0:7:3],
                     self.str[1:8:3], self.str[2:9:3], self.str[0:9:4], self.str[2:7:2]]
        if "XXX" in self.case:
            print("X wins")
            self.win = True
        elif "OOO" in self.case:
            print("O wins")
            self.win = True
        return self.win

    def draw_check(self):
        self.x_count = self.cells.count("X")
        self.o_count = self.cells.count("O")
        if (self.x_count + self.o_count) == 9:
            print("Draw")
            return True

    def play_game(self):
        print(self.drawing_field())
        while True:
            self.players_input()
            if self.win_test():
                break
            elif self.draw_check():
                break

game = TicTacToe()
game.play_game()
