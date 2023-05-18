import copy

board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]

#define min and max for alpha and beta
MIN = float('-inf') #for alpha = -infinity
MAX = float('inf') #for beta  = infinity 

# Constants for the board size
ROW_COUNT = 6
COLUMN_COUNT = 7

# Constants for the computers
computer = 0
AI = 1

computer_PIECE = 1
AI_PIECE = 2


def put_piece(board, col, piece):
    for row in range(ROW_COUNT-1,-1,-1):
        if board[row][col] == 0:
            board[row][col] = piece
            return	

def is_terminal(board):
    return False

def is_winning(board,piece):
    return False

def get_score(board, piece):
    return 100

def minimax(board, depth, is_max): 
	flag = is_terminal(board)
	if depth == 0 or flag:
		if flag:
			if is_winning(board, AI_PIECE):
				return (0, MAX)
			elif is_winning(board, computer_PIECE):
				return (0, MIN)
			else: # Game is over, no more valid moves
				return (0, 0)
		else: # Depth is zero
			return (0, get_score(board, AI_PIECE))
    # if it isn't the terminal node continue 
    # get the empty or valid colume 
	empty_locations = []
	for col in range(COLUMN_COUNT):
		if board[0][col] == 0:
			empty_locations.append(col)

	if is_max:
		value = MIN
		column = empty_locations[0]
		for location in empty_locations:
			board_copy = copy.deepcopy(board)
			put_piece(board_copy, location, AI_PIECE)
			new_value = minimax(board_copy, depth-1, False)[1]
			if new_value > value:
				value = new_value
				column = location
			
		return column, value
	else: # Minimizing computer
		value = MAX
		column =empty_locations[0]
		for location in empty_locations:
			board_copy = copy.deepcopy(board)
			put_piece(board_copy,location, computer_PIECE)
			new_value = minimax(board_copy, depth-1, True)[1]
			if new_value < value:
				value = new_value
				column = location
			
		return column, value

