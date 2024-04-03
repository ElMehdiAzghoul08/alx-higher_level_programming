#!/usr/bin/python3
"""N-queens
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = [[" " for _ in range(n)] for _ in range(n)]
    return board


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    return [row[:] for row in board]


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
    return solution


def xout(board, row, col):
    """X out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    n = len(board)
    # X out all forward spots
    for c in range(col + 1, n):
        board[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, n):
        board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all spots diagonally down to the right
    for r, c in zip(range(row + 1, n), range(col + 1, n)):
        board[r][c] = "x"
    # X out all spots diagonally up to the left
    for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        board[r][c] = "x"
    # X out all spots diagonally up to the right
    for r, c in zip(range(row - 1, -1, -1), range(col + 1, n)):
        board[r][c] = "x"
    # X out all spots diagonally down to the left
    for r, c in zip(range(row + 1, n), range(col - 1, -1, -1)):
        board[r][c] = "x"


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    n = len(board)
    if queens == n:
        solutions.append(get_solution(board))
        return solutions

    for c in range(n):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(n)
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
        