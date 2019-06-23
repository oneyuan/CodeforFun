#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (40.94%)
# Likes:    2567
# Dislikes: 58
# Total Accepted:    228.6K
# Total Submissions: 558.3K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
# 
# Example:
# 
# 
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4. 
# 
# Note: 
# 
# 
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n^2) complexity.
# 
# 
# Follow up: Could you improve it to O(n log n) time complexity?
# 
#
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        res = 0
        if n == 0:
            return 0
        for i in range(n):
            maxval = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    maxval = max(maxval, dp[j])
            dp[i] = maxval + 1
            res = max(res, dp[i])
        return res

    def lengthOfLIS0(self, nums: List[int]) -> int:
        # consider the longest increasing subsequence
        if len(nums) <= 1: return len(nums)
        n = len(nums)
        lis = [0]*n
        p = 1
        lis[0] = nums[0]
        for i in range(1, n):
            if nums[i] > lis[p-1]:
                lis[p] = nums[i]
                p += 1
            elif nums[i] < lis[0]:
                lis[0] = nums[i]
            else:
                # our value is somewhere in the midddle, find the location
                j = bisect.bisect_left(lis, nums[i], 0, p)
                # if the value actually exists in our array, do nothing
                if lis[j] != nums[i]:
                    # the leading element of lis[j] will now be smaller than it was before
                    lis[j] = nums[i]
        return p

