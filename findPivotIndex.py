"""
Given an array of integers nums, write a method that returns the "pivot" index of this array.
We define the pivot index as the index where the sum of the numbers to the left of the index is equal
to the sum of the numbers to the right of the index.
If no such index exists, we should return -1. If there are multiple pivot indexes,
you should return the left-most pivot index.

https://leetcode.com/problems/find-pivot-index/
"""


def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    SumNums = sum(nums)
    if len(nums) == 0:
        return -1

    for i in range(0,len(nums)):
        if i == 0:
            leftS = 0
            rightS = SumNums - nums[0]
        else:
            leftS = leftS + nums[i-1]
            rightS = SumNums - nums[i] - leftS
        if leftS == rightS:
            return i

    return -1


def test():
    assert pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert pivotIndex([1, 2, 3]) == -1

