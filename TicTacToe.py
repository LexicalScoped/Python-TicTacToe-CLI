class Game():
    def __init__(self):
        self.board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
        self.turn = "x"
        self.state = True
        self.turn_counter = 0

    def print_board(self):
        for i in range(3):
            print(" " + self.board[i][0] + " | " + self.board[i][1] + " | " + self.board[i][2])
            if i != 2:
                print('---+---+---')

    def move_input(self, xy):
        xy = xy.replace(" ", "")
        if len(xy) != 2 or not xy.isnumeric():
            print("Invalid Input\n")
            return
        for loc in xy:
            if int(loc) > 3 or int(loc) < 1:
                print("Invalid Input\n")
                return
        self.make_move(int(xy[0]) - 1, int(xy[1]) - 1)

    def make_move(self, x, y):
        if not self.board[x][y] == " ":
            print("Location already filled\n")
            return
        self.board[x][y] = self.turn
        self.evaluate()
        if self.turn == "x":
            self.turn = "o"
        else:
            self.turn = "x"
        self.turn_counter += 1

    def evaluate(self):     
        for i in range(3):
            if self.board[i][0] == self.turn and self.board[i][1] == self.turn and self.board[i][2] == self.turn:
                self.state = False
            if self.board[0][i] == self.turn and self.board[1][i] == self.turn and self.board[2][i] == self.turn:
                self.state = False
        if self.board[0][0] == self.turn and self.board[1][1] == self.turn and self.board[2][2] == self.turn:
            self.state = False 
        elif self.board[2][0] == self.turn and self.board[1][1] == self.turn and self.board[0][2] == self.turn:
            self.state = False

        if self.state == False:
            self.print_board()
            print(self.turn + " has won the game.")
        elif self.turn_counter == 9:
            self.print_board()
            self.state = False
            print("the game is a draw")

def main():
    while True:
        menu_response = input("Would you like to play a game? [y/n]: ")
        if menu_response.lower() != "n" and menu_response.lower() != "y":
            print("invalid menu selection")
            continue
        elif menu_response.lower() == "n":
            break
        game = Game()
        while game.state:
            game.print_board()
            game.move_input(input("input x y coordinates : "))

if __name__ == "__main__":
    main()