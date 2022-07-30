"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None
CONSECUTIVETOWIN = 3


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    # Count plays made by each player
    x_plays = sum(x.count(X) for x in board)
    o_plays = sum(x.count(O) for x in board)
    if x_plays <= o_plays:
        return X
    return O


def actions(board):
    moves = []
    # If terminal state --> returns empty
    if not terminal(board):
        i = 0
        j = 0
        # Search for cells that are EMPTY
        for row in board:
            for cell in row:
                if cell == EMPTY:
                    # If cell is empty --> coordinate is appended
                    moves.append((i, j))
                j = j + 1
            j = 0
            i = i + 1

    return moves


def result(board, action):
    p = player(board)
    # If game has finished, an error is raised
    if terminal(board):
        raise ActionException("Game has finished")
    # Search for cell and check if empty
    cell = get_cell(board, action)
    if cell != EMPTY:
        raise ActionException("Cell is occupied")

    b = copy.deepcopy(board)
    b[action[0]][action[1]] = p
    return b


def winner(board):
    row_n = 0
    if len(board) <= 1:
        raise BoardException("Board size must be greatear than 2")

    # Check winner horizontally
    for row in board:
        symbol = row[0]
        # If symbol is not none, I check diagonal
        if symbol is EMPTY:
            consecutive = 0
        else:
            consecutive = 1
            win = check_diagonal_win(board, row_n, 0, symbol)
            if win is not None:
                return win

        for column_n in range(1, len(row)):
            # If symbol is Emoty, we skip til a symbol is found
            if row[column_n] is EMPTY:
                consecutive = 0
                symbol = row[column_n]
            else:
                if symbol == row[column_n]:
                    consecutive = consecutive + 1
                    if consecutive == CONSECUTIVETOWIN:
                        return symbol
                else:
                    symbol = row[column_n]
                    consecutive = 1

                win = check_diagonal_win(board, row_n, column_n, symbol)
                if win is not None:
                    return win

        row_n = row_n + 1
        consecutive = 0

    # Last check to make is horizontal win
    return check_vertical_win(board)


def terminal(board):
    t, w = terminal_and_winner(board)
    return t


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    return player_utility(w)


def minimax(board):
    move, value = minimax_value(board, -math.inf, math.inf)
    return move


def minimax_value(board, alpha, beta):
    """
    Returns the optimal action for the current player on the board.
    """
    t, w = terminal_and_winner(board)
    if t:
        return None, player_utility(w)

    moves = actions(board)
    play = None
    if player(board) == X:
        for move in moves:
            _, value = minimax_value(result(board, move), alpha, beta)
            if value > alpha:
                alpha = value
                play = move
            if beta <= alpha:
                return play, alpha
        return play, alpha

    else:
        for move in moves:
            _, value = minimax_value(result(board, move), alpha, beta)
            if value < beta:
                beta = value
                play = move
            if beta <= alpha:
                return play, beta
        return play, beta


def terminal_and_winner(board):
    w = winner(board)

    if w is not None:
        return True, w

    for row in board:
        for cell in row:
            if cell is EMPTY:
                return False, None

    return True, None


class ActionException(Exception):
    pass


class BoardException(Exception):
    pass


def get_cell(board, action):
    if action[0] > len(board) - 1:
        raise IndexError
    row = board[action[0]]
    if action[1] > len(row) - 1:
        raise IndexError
    return row[action[1]]


def check_diagonal_win(board, row_n, column_n, symbol):
    # Check diagonal win
    max_row_diag_check = row_n + CONSECUTIVETOWIN - 1
    max_column_diag_check = column_n + CONSECUTIVETOWIN - 1
    if max_row_diag_check < len(board) and max_column_diag_check < len(board[row_n]):
        i = row_n + 1
        j = column_n + 1
        while i <= max_row_diag_check and j <= max_column_diag_check and symbol == board[i][j]:
            i = i + 1
            j = j + 1
        if i > max_row_diag_check:
            return symbol

    # Check inverse diagonal win
    max_row_diag_check = row_n + CONSECUTIVETOWIN - 1
    max_column_diag_check = column_n - CONSECUTIVETOWIN + 1
    if max_row_diag_check < len(board) and max_column_diag_check >= 0:
        i = row_n + 1
        j = column_n - 1
        while i <= max_row_diag_check and j >= max_column_diag_check and symbol == board[i][j]:
            i = i + 1
            j = j - 1
        if i > max_row_diag_check:
            return symbol
    return None


def check_vertical_win(board):
    # Check winner vertically
    for column_n in range(len(board[0])):
        symbol = board[0][column_n]
        consecutive = 1
        for row_n in range(1, len(board)):
            if board[row_n][column_n] is EMPTY:
                consecutive = 0
                symbol = board[row_n][column_n]
            if symbol == board[row_n][column_n]:
                consecutive = consecutive + 1
                if consecutive == CONSECUTIVETOWIN:
                    return symbol
            else:
                symbol = board[row_n][column_n]
                consecutive = 1


def player_utility(p):
    if p == X:
        return 1
    else:
        if p == O:
            return -1
        else:
            return 0
