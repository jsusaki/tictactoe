"""
    Introduction to Computer Programming in Python: A Hands-on Approach
    Part 0: Tic-Tac-Toe Object, Board Representation and Print Board Function
"""
# Create the Tic-Tac-Toe class that represents the Game itself
class TicTacToe(object):
    def __init__(self):
        # Represent the board
        self.board = [
            ['X','X','O'], # First Line
            ['X','O','X'], # Second Line
            ['X',' ','O']  # Third Line
        ]

    # Initialize Board Function
    def InitBoard(self):
        for i in range(0, 3):
            for j in range(0, 3):
                self.board[i][j] = ' '

    # Print Board Function for Visual Feedback
    def PrintBoard(self, board):
        print() # New line
        # For each line in the 2x2 board (index 0 counting)
        for i in range(0, 3):            
            # For each column in the 2x2 board
            for j in range(0, 3):
                # Print the element at position i, j in the array
                print(str(self.board[i][j]), end=' ')
            print()

if __name__ == "__main__":

    print("Tic-Tac-Toe Part 0")

    # Instantiate the TicTacToe object
    game = TicTacToe()

    # Call the Print Board Member Function
    game.PrintBoard(game.board)
    