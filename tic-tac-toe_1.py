"""
    Introduction to Computer Programming in Python: A Hands-on Approach
    Part 1: Player Representation, Move and Input Function
"""

class TicTacToe(object):
    def __init__(self):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        # Represent Players as char
        self.playerX = 'X'
        self.playerO = 'O'

        self.MoveValid = False
        self.InputValid = False

    def InitBoard(self):
        for i in range(0, 3):
            for j in range(0, 3):
                self.board[i][j] = ' '

    def PrintBoard(self, board):
        print()
        for i in range(0, 3):            
            for j in range(0, 3):
                print(str(self.board[i][j]), end=' ')
            print()

    # Get Input Fuction
    def GetInput(self):
        self.InputValid = False
        # While input is not valid
        while not self.InputValid:
            # Get Input Position(x, y), where player wants to play 
            x = int(input("Specify a coordinate for x: "))
            y = int(input("Specify a coordinate for y: "))

            # Check if input is within the board boundry
            if x < 0 or x > 2 and y < 0 or y > 2:
                print("Invalid Input, the coordinate should be a number between 0 and 2 for x and y")
                continue
            else: # If so, input is valid, and return the specified position
                self.InputValid = True          
                return x, y

    # Make Move Function, take board, player, x and y
    def MakeMove(self, board, player, x, y):        
        self.MoveValid = False
        # While move is not valid
        while not self.MoveValid:
            # Check if the specified position is not occupied
            if self.board[x][y] == ' ':
                # If so, make move by placing the player symbol into the specified board position
                self.board[x][y] = player
                self.MoveValid = True
            else: # If move is not valid, break the loop and return to GetInput Function
                break

if __name__ == "__main__":

    print("Tic-Tac-Toe Part 1")
    game = TicTacToe()
    game.InitBoard()
    # Check if make move function works as expected
    #game.MakeMove(game.board, 'X', 2, 2)

    # Get input from player
    x, y = game.GetInput()

    # Make move at specified position
    game.MakeMove(game.board, 'X', x, y)

    game.PrintBoard(game.board)