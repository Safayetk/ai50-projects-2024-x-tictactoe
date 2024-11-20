"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError("Invalid action")
    new_board = [row[:] for row in board]  # Deep copy
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # Check columns for a winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    # If no winner
    return None


def terminal(board):
    """
    Returns True if the game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    def max_value(board):
        if terminal(board):
            return utility(board)
        v = float('-inf')
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = float('inf')
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    best_action = None
    if current_player == X:
        best_value = float('-inf')
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
    else:
        best_value = float('inf')
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action

    return best_action


if __name__ == "__main__":
    # Test case 1: Game is not over (still empty cells)
    board1 = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", None]
    ]
    print("Test case 1:", terminal(board1))  # Expected: False

    # Test case 2: Game is over (X wins horizontally)
    board2 = [
        ["X", "X", "X"],
        ["O", "O", None],
        [None, None, None]
    ]
    print("Test case 2:", terminal(board2))  # Expected: True

    # Test case 3: Game is over (O wins diagonally)
    board3 = [
        ["O", "X", None],
        ["X", "O", None],
        [None, None, "O"]
    ]
    print("Test case 3:", terminal(board3))  # Expected: True

    # Test case 4: Game is over (board is full, no winner)
    board4 = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "O"]
    ]
    print("Test case 4:", terminal(board4))  # Expected: True

    # Test case 5: Actions available on the board
    board5 = [
        ["X", "O", None],
        ["O", None, None],
        [None, "X", "O"]
    ]
    print("Test case 5:", actions(board5))  # Expected: {(0, 2), (1, 1), (1, 2), (2, 0)}

    # Test case 6: Resulting board after an action
    board6 = [
        ["X", "O", None],
        ["O", None, None],
        [None, "X", "O"]
    ]
    action = (0, 2)
    print("Test case 6:", result(board6, action))
    # Expected: [["X", "O", "X"], ["O", None, None], [None, "X", "O"]]

    # Test case 7: Winner determination
    board7 = [
        ["X", "X", "X"],
        ["O", "O", None],
        [None, None, None]
    ]
    print("Test case 7:", winner(board7))  # Expected: "X"

    board8 = [
        ["O", "X", None],
        ["X", "O", None],
        [None, None, "O"]
    ]
    print("Test case 8:", winner(board8))  # Expected: "O"

    board9 = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "O"]
    ]
    print("Test case 9:", winner(board9))  # Expected: None (no winner)
