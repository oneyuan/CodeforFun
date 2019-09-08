#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                return i
        return n-1

    def findPeakElement(self, A: List[int]) -> int:
        if not A:
            return -1
        if len(A) == 1:
            return 0
        if A[0] > A[1]:
            return 0
        if A[-1] > A[-2]:
            return len(A) - 1
        for i in range(1, len(A) - 1):
            if A[i - 1] < A[i] and A[i + 1] < A[i]:
                return i
        return -1

