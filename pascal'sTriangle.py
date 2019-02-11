"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
https://leetcode.com/problems/pascals-triangle/
"""


def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    matrix = [[1 for j in range(i+1)] for i in range(0, numRows)]
    if numRows > 2:
        for i in range(2, numRows):
            for j in range(1, i):
                matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]
    return matrix


def test():
    assert generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert generate(6) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]

