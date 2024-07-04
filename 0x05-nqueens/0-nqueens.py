#!/usr/bin/python3
"""Module for N queens solution finder."""
import sys


solutions = []  # The list of possible solutions to the N queens problem.

def get_input():
    """Program arguments are retrieved and validated."""
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
    return n

def is_attacking(pos0, pos1):
    """
    Checking whether the positions of two
    queens are in an attacking mode.
    """
    return (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]) or \
           (abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1]))

def group_exists(group):
    """Confirming whether a group exists in the list of solutions."""
    return any(set(stn) <= set(group) for stn in solutions)

def build_solution(row, group):
    """A solution for the n queens problem is built."""
    if row == n:
        tmp0 = group.copy()
        if not group_exists(tmp0):
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip([pos[a]] * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(pos[a].copy())
            if not any(used_positions):
                build_solution(row + 1, group)
            group.pop()

def get_solutions():
    """Getting the solutions for the given chessboard size."""
    global pos, n
    pos = [[x // n, x % n] for x in range(n ** 2)]
    a = 0
    group = []
    build_solution(a, group)

n = get_input()
get_solutions()
for solution in solutions:
    print(solution)
