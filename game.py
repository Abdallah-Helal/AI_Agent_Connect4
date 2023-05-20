from board import Board
import time
import random
from board import *
from Minimax import *

# GAME LINK
# http://kevinshannon.com/connect4/

#define min and max for alpha and beta
MIN = float('-inf') #for alpha = -infinity
MAX = float('inf') #for beta  = infinity 

def main():
    board = Board()

    time.sleep(2)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        board.print_grid(game_board)
        print("\n")
        bestc,score = minimax_AlphaBeta(game_board,6,MIN,MAX,True)
        #  bestc,score = minimax(game_board,3,True)
        print(bestc)
        # YOUR CODE GOES HERE

        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column
        #random_column = random.randint(0, 6)
        board.select_column(bestc)

        time.sleep(2)


if __name__ == "__main__":
    main()
