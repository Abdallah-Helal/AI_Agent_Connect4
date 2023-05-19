import copy

YELLOW = (255, 255, 0)
White = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

# define min and max for alpha and beta
MIN = float('-inf')  # for alpha = -infinity
MAX = float('inf')  # for beta  = infinity

# Constants for the board size
ROW_COUNT = 6
COLUMN_COUNT = 7

SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE+2*SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE+SQUARESIZE/2


RADIUS = int(SQUARESIZE/2 - 5)

# Constants for the computers
computer = 0
AI = 1

computer_PIECE = 1
AI_PIECE = 2

# Constants for the evaluation function
WINNING_SCORE = 1000000
THREE_IN_A_ROW_SCORE = 100
TWO_IN_A_ROW_SCORE = 10
ONE_IN_A_ROW_SCORE = 1

game_over = False
turn = computer


def print_board(board):
    for row in range(ROW_COUNT):
        print(board[row])
    print('\n')


def put_piece(board, col, piece):
    for row in range(ROW_COUNT-1, -1, -1):
        if board[row][col] == 0:
            board[row][col] = piece
            return

# Check horizontal locations for win


def check_horizontal(board, piece):
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT-3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True
    return False

# Check vertical locations for win


def check_vertical(board, piece):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True
    return False

# Check positively sloped diagonals


def check_diagonal(board, piece):
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True
    return False

# Check negatively sloped diagonals


def check_rev_diagonal(board, piece):
    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True

    return False


def is_winning(board, piece):
    if(check_horizontal(board, piece) or check_vertical(board, piece) or check_diagonal(board, piece) or check_rev_diagonal(board, piece)):
        return True
    return False


def is_terminal(board):
    empty_locations = []
    for col in range(COLUMN_COUNT):
        if board[0][col] == 0:
            empty_locations.append(col)

    return is_winning(board, computer_PIECE) or is_winning(board, AI_PIECE) or len(empty_locations) == 0


def evaluate_score(array, piece):
    score = 0
    opp_piece = computer if piece == AI else AI

    if array.count(piece) == 4:
        score += WINNING_SCORE
    elif array.count(piece) == 3 and array.count(0) == 1:
        score += THREE_IN_A_ROW_SCORE
    elif array.count(piece) == 2 and array.count(0) == 2:
        score += TWO_IN_A_ROW_SCORE
    elif array.count(piece) == 1 and array.count(0) == 3:
        score += ONE_IN_A_ROW_SCORE

    if array.count(opp_piece) == 3 and array.count(0) == 1:
        score -= THREE_IN_A_ROW_SCORE
    elif array.count(opp_piece) == 2 and array.count(0) == 2:
        score -= TWO_IN_A_ROW_SCORE
    elif array.count(opp_piece) == 1 and array.count(0) == 3:
        score -= ONE_IN_A_ROW_SCORE

    return score


def get_score(board, piece):
    score = 0

    # Score center column
    center_count = sum(row[COLUMN_COUNT // 2] == piece for row in board)
    score += center_count * 3

    # Score Horizontal
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT-3):
            # Extract a small_board of 4 adjacent cells
            small_board = [board[row][col+i] for i in range(4)]
            score += evaluate_score(small_board, piece)

    # Score Vertical
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT-3):
            # Extract a small_board of 4 adjacent cells
            small_board = [board[row+i][col] for i in range(4)]
            score += evaluate_score(small_board, piece)

    # Score positive sloped diagonal
    for row in range(ROW_COUNT - 3):
        for col in range(COLUMN_COUNT - 3):
            # Extract a small_board of 4 adjacent cells
            small_board = [board[row+i][col+i] for i in range(4)]
            score += evaluate_score(small_board, piece)

    # Score negative sloped diagonal
    for row in range(ROW_COUNT - 3):
        for col in range(COLUMN_COUNT - 3):
            # Extract a small_board of 4 adjacent cells
            small_board = [board[row+3-i][col+i] for i in range(4)]
            score += evaluate_score(small_board, piece)

    return score


def minimax_AlphaBeta(board, depth, alpha, beta, maximizing):
    flag = is_terminal(board)
    if depth == 0 or flag:
        if flag:
            if is_winning(board, AI_PIECE):
                return (0, MAX)
            elif is_winning(board, computer_PIECE):
                return (0, MIN)
            else:  # Game is over, no more valid moves
                return (0, 0)
        else:  # Depth is zero
            return (0, get_score(board, AI_PIECE))
    # if it isn't the terminal node continue
    # get the empty or valid colume
    empty_locations = []
    for col in range(COLUMN_COUNT):
        if board[0][col] == 0:
            empty_locations.append(col)

    if maximizing:
        value = MIN
        column = empty_locations[0]
        for location in empty_locations:
            board_copy = copy.deepcopy(board)
            put_piece(board_copy, location, AI_PIECE)
            new_value = minimax_AlphaBeta(
                board_copy, depth-1, alpha, beta, False)[1]
            if new_value > value:
                value = new_value
                column = location
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    else:  # Minimizing computer
        value = MAX
        column = empty_locations[0]
        for location in empty_locations:
            board_copy = board.copy()
            put_piece(board_copy, location, computer_PIECE)
            new_value = minimax_AlphaBeta(
                board_copy, depth-1, alpha, beta, True)[1]
            if new_value < value:
                value = new_value
                column = location
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


def minimax(grid, depth, is_max):
    flag = is_terminal(grid)
    if depth == 0 or flag:
        if flag:
            if is_winning(grid, AI_PIECE):
                return (0, MAX)
            elif is_winning(grid, computer_PIECE):
                return (0, MIN)
            else:  # Game is over, no more valid moves
                return (0, 0)
        else:  # Depth is zero
            return (0, get_score(grid, AI_PIECE))
    # if it isn't the terminal node continue
    # get the empty or valid colume
    empty_locations = []
    for col in range(COLUMN_COUNT):
        if grid[0][col] == 0:
            empty_locations.append(col)

    if is_max:
        value = MIN
        column = empty_locations[0]
        for location in empty_locations:
            grid_copy = copy.deepcopy(grid)
            put_piece(grid_copy, location, AI_PIECE)
            new_value = minimax(grid_copy, depth-1, False)[1]
            if new_value > value:
                value = new_value
                column = location

        return column, value
    else:  # Minimizing computer
        value = MAX
        column = empty_locations[0]
        for location in empty_locations:
            grid_copy = copy.deepcopy(grid)
            put_piece(grid_copy, location, computer_PIECE)
            new_value = minimax(grid_copy, depth-1, True)[1]
            if new_value < value:
                value = new_value
                column = location

        return column, value
