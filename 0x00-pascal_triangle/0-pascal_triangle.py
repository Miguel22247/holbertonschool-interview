#!/usr/bin/python3
""" Pascal Triangle """


def pascal_triangle(n):
    """calculates pascal and returns a list"""
    pascal_list = []

    if n <= 0:
        return pascal_list

    for i in range(n):
        temp_list = []
        for j in range(i + 1):
            if (j == 0 or j == i):
                temp_list.append(1)
            else:
                temp_list.append(pascal_list[i-1][j-1] + pascal_list[i-1][j])
        pascal_list.append(temp_list)
    return pascal_list
