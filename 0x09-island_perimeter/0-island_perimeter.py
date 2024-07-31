#!/usr/bin/python3
"""
Function to calculate the perimeter of the island in the grid.
"""


def island_perimeter(grid):
    """Calculates the perimeter of the island described in the grid."""
    perimeter = 0
    if not isinstance(grid, list):
        return 0

    rows = len(grid)

    for i in range(rows):
        row = grid[i]
        cols = len(row)

        for j in range(cols):
            if row[j] == 1:
                if i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0):
                    perimeter += 1
                if i == rows - 1 or (len(grid[i + 1]) > j and
                                     grid[i + 1][j] == 0):
                    perimeter += 1
                if j == 0 or row[j - 1] == 0:
                    perimeter += 1
                if j == cols - 1 or (cols > j + 1 and row[j + 1] == 0):
                    perimeter += 1

    return perimeter
