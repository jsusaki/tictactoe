"""
    Introduction to Computer Programming in Python: A Hands-on Approach
    Part 2: Game Loop, Change Turn and Win Condition
"""

class TicTacToe(object):
    def __init__(self):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        
        self.playerX = 'X'
        self.playerO = 'O'

        # Initialize Turn Counter
        self.turn = 1

        # Initialize First Player
        self.currentPlayer = self.playerX

        # Initialize Win Condition
        self.win = False

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

        print("Turn: " + str(self.turn))
        print("Current Player: " + str(self.currentPlayer))

        if self.win == True:
            print("Winner: Player " + self.currentPlayer + "!")     

    def MakeMove(self, board, player, x, y):        
        self.MoveValid = False
        while not self.MoveValid:
            if self.board[x][y] == ' ':
                self.board[x][y] = player
                self.turn += 1
                self.MoveValid = True
            else:
                break

    def ChangeTurn(self, currentPlayer):
        # Check if move is valid and the game is not won
        if self.MoveValid and not self.win:
            # If so, check current player
            if self.currentPlayer == self.playerX:
                # If current player is 'X', set the current player to 'O'
                self.currentPlayer = self.playerO
            else: # Otherwise, set the current player to 'X'
                self.currentPlayer = self.playerX

    def CheckWinCondition(self, board):
        """
        Horizontal
         X | X | X     |   |       |   |     
        ---+---+--- ---+---+--- ---+---+---
           |   |     X | X | X     |   |       
        ---+---+--- ---+---+--- ---+---+---
           |   |       |   |     X | X | X   

        Vertical
         X |   |       | X |       |   | X    
        ---+---+--- ---+---+--- ---+---+---
         X |   |       | X |       |   | X      
        ---+---+--- ---+---+--- ---+---+---
         X |   |       | X |       |   | X  

        Diagonal
         X |   |       |   | X
        ---+---+--- ---+---+---
           | X |       | X |         
        ---+---+--- ---+---+--- 
           |   | X   X |   |
        """ 
        # Check for horizontal line
        if (self.board[0][0] == self.board[0][1] == self.board[0][2] == self.currentPlayer) or \
           (self.board[1][0] == self.board[1][1] == self.board[1][2] == self.currentPlayer) or \
           (self.board[2][0] == self.board[2][1] == self.board[2][2] == self.currentPlayer): 
           self.win = True
           return self.win

        # Check for vertical line
        elif (self.board[0][0] == self.board[1][0] == self.board[2][0] == self.currentPlayer) or \
             (self.board[0][1] == self.board[1][1] == self.board[2][1] == self.currentPlayer) or \
             (self.board[0][2] == self.board[1][2] == self.board[2][2] == self.currentPlayer): 
             self.win = True
             return self.win

        # Check for diagonal line
        elif (self.board[0][0] == self.board[1][1] == self.board[2][2] == self.currentPlayer) or \
             (self.board[0][2] == self.board[1][1] == self.board[2][0] == self.currentPlayer): 
             self.win = True
             return self.win

        return False

    def GetInput(self):
        self.InputValid = False
        while not self.InputValid:
            x = int(input("Specify a coordinate for x: "))
            y = int(input("Specify a coordinate for y: "))

            if x < 0 or x > 2 and y < 0 or y > 2:
                print("Invalid Input, the coordinate should be a number between 0 and 2 for x and y")
                continue
            else:
                self.MoveValid = True          
                return x, y

if __name__ == "__main__":

    print("Welcome to Simple Tic-Tac-Toe!")
    game = TicTacToe()
    game.InitBoard()
    
    # GAME LOOP
    while not game.win:
        # INPUT
        x, y = game.GetInput()

        # UPDATE GAME LOGIC
        game.MakeMove(game.board, game.currentPlayer, x, y)
        game.CheckWinCondition(game.board)
        game.ChangeTurn(game.currentPlayer)

        # RENDER
        game.PrintBoard(game.board)