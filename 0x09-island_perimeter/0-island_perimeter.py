#!/usr/bin/python3
"""Island perimeter
"""


def island_perimeter(grid):
    """Calculates the perimeter of an island, grid
    """
    per = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                per += 4
                if i > 0:
                    per = per - grid[i - 1][j]
                if i < len(grid) - 1:
                    per = per - grid[i + 1][j]
                if j > 0:
                    per = per - grid[i][j - 1]
                if j < len(grid) - 1:
                    per = per - grid[i][j + 1]
    return per
