import unittest
"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
https://leetcode.com/problems/rotate-array/
"""


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        nums.insert(0, nums[len(nums)-1])
        nums.pop(len(nums)-1)
