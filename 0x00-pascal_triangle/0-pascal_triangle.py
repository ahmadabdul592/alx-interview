#!/usr/bin/python3
'''
    Pascal's Triangle.
'''


def pascal_triangle(n):
    '''
        Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    if type(n) is not int or n <= 0:
        return ([])
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    triangle = [[1], [1, 1]]
    for i in range(2, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
