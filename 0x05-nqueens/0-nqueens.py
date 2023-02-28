#!/usr/bin/python3
""" 
N-Queens Module
"""
import sys


def is_valid(board, row, col):
    """ Check if valid """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_n_queens(n, row, board, solutions):
    """ Solve """
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            solve_n_queens(n, row + 1, board, solutions)
            board[row] = -1


def print_solutions(solutions):
    """ Print solutions """
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve_n_queens(n, 0, board, solutions)
    print_solutions(solutions)
