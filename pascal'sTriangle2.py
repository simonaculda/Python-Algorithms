"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
https://leetcode.com/problems/pascals-triangle-ii/
"""


def getRow(numRows):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    matrix = [[1 for j in range(i+1)] for i in range(0, numRows+1)]
    if numRows >= 2:
        for i in range(2, numRows+1):
            for j in range(1, i):
                matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]
    return matrix[numRows][:]


def test():
    assert getRow(3) == [1, 3, 3, 1]
    assert getRow(4) == [1, 4, 6, 4, 1]

