"""
    Introduction to Computer Programming in Python: A Hands-on Approach

    A Minimal and Simple Tic-Tac-Toe Program in Python 
        76 lines of code without new lines and comments
        This computer program is designed for computer programming introduction tutorial 
        oriented towards an advanced (curious, determined, persistent, disciplined) learner.

        - You will learn how to program only by reading and writing lot of programs.
        - You will learn how to design systems only by designing systems.

    Objective
        Learn how to 1) Analyze, 2) Design and 3) Implement computer program 
        written in python programming language.

    Process
        1. Analysis: Analysis phase consists of understanding the problem.
        2. Design: Design phase consists of decomposing the problem in different parts.
        3. Implementation: Implementation phase consists of implementing 
        the designed parts in specific programming language.

    Problem
        Tic-Tac-Toe Game

    1. Analysis
        Tic-Tac-Toe is a two player turn-based zero-sum perfect information game, 
        which in a 3x3 grid board, each player take a turn and make a move using the symbol 'X' or 'O'. 
        The player that completes a horizontal, vertical or diagonal line in the board win the game.    

    2. Design
        In order to design a tic-tac-toe program, we will directly translate the concepts defined in the analysis phase. 

        The Tic-Tac-Toe is composed of:
            3x3 Board
            2 Players
            Turn
            Move
            Symbol: 'X' and 'O'
            Win Condition: A horizontal, vertical, diagonal line.

        After the problem decomposition, we will map and represent each concept in a data structure (data) 
        and algorithms (functions). Program = Data Structure + Algorithm

        Data Structure
            Board
                3 x 3 board
                
                 X | X | X 
                ---+---+---
                 X | O | X  
                ---+---+---
                 X | O | O  

            Player
                Player 1: 'X'
                Player 2: 'O'

            Turn
                Positive number to indicate game turn

        Algorithms
            Move
                Function to make a move
        
            Win Condition
                Function to check if one of the player wins or not
                    Check Horizontal Line
                    Check Vertical Line
                    Check Diagonal Line

        Pseudo-Code
            Pseudo-Code is a simplified notation that informs the overall program structure. 
            It is in-between the natural langauge and programming language. 
            It is useful to sketch the program before implementation.

            while game is not over:
                take input from current player
                make move in the board
                if current player forms a line in the board
                    game is over: current player win the game
                else
                    game is not over: continue the loop
                change turn                

    3. Implementation
        We will implement using computer programming language what we designed in the design phase.

    Future Extension:
        AI class
            Random
            Search Algorithms
            Neural Network
            Reinforcement Learning

        Implement it in C++

Created: 25/10/2020
Last Updated: 25/10/2020
Author: femto
"""

# Create a Tic-Tac-Toe Object
class TicTacToe(object):
    def __init__(self):
        # Define Board
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        # Define Players
        self.playerX = 'X'
        self.playerO = 'O'
        # Initialize Turn
        self.turn = 1
        # Define Starting Player
        self.currentPlayer = self.playerX
        # Define Win Condition
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
        if self.MoveValid and not self.win:
            if self.currentPlayer == self.playerX:
                self.currentPlayer = self.playerO
            else:
                self.currentPlayer = self.playerX

    def CheckWinCondition(self, board):
        # Check for vertical line
        if (self.board[0][0] == self.board[0][1] == self.board[0][2] == self.currentPlayer) or \
           (self.board[1][0] == self.board[1][1] == self.board[1][2] == self.currentPlayer) or \
           (self.board[2][0] == self.board[2][1] == self.board[2][2] == self.currentPlayer): 
           self.win = True
           return self.win

        # Check for horizontal line
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

            # Check Invalid Input
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