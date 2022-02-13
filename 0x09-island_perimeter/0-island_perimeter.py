#!/usr/bin/python3
"""Python code that returns the perimeter where 0 is water and 1 is land"""


def island_perimeter(grid):
    """Land is 1 and water is 0"""
    land = 1
    water = 0
    perimeter = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == land:
                if y == 0 or grid[y + 1][x] == water:
                    perimeter += 1
                if y == len(grid) - 1 or grid[y + 1][x] == WATER:
                    perimeter += 1
                if x == 0 or grid[y][x - 1] == WATER:
                    perimeter += 1
                if x == len(row) - 1 or grid[y][x + 1] == WATER:
                    perimeter += 1
    return perimeter
