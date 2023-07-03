#!/usr/bin/python3
"""Solves the N-queens puzzle."""

import sys

def is_safe(board, row, col, N):
    """Check if there is a queen in the same column"""
    for i in range(row):
        if board[i][col] == 1:
            return False

    """Check if there is a queen in the upper 
        left diagonal"""
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    """Check if there is a queen in the upper 
        right diagonal"""
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(N):
    """Return the list of lists representation of a solved chessboard."""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def backtrack(row):
        if row == N:
            solution = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
        else:
            for col in range(N):
                if is_safe(board, row, col, N):
                    board[row][col] = 1
                    backtrack(row + 1)
                    board[row][col] = 0

    backtrack(0)
    return solutions

def print_solutions(solutions):
    """Return the list of lists representation 
        of a solved chessboard."""
    for solution in solutions:
        print(solution)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)
