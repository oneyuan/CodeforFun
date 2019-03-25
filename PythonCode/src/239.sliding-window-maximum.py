#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (36.89%)
# Total Accepted:    144K
# Total Submissions: 385K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
# 
# Example:
# 
# 
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7] 
# Explanation: 
# 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty
# array.
# 
# Follow up:
# Could you solve it in linear time?
#
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1 or k == 0:
            return nums

        def findMax(nums):
            n = len(nums)
            max_value = float('-inf')
            #second = float('-inf')
            for i in range(k):
                if nums[i] > max_value:
                        max_value = nums[i]
            return max_value

        res = []
        n = len(nums)
        max_value = findMax(nums[:k])
        for j in range(k-1, n):
            if nums[j] > max_value:
                max_value = nums[j]
            elif nums[j-k] == max_value:
                max_value = findMax(nums[j-k+1:j+1])
            res.append(max_value)
        return res

    def maxSlidingWindow0(self, nums, k):
        if not nums or k == 0:
            return []
        reuslt = [0] * (len(nums) - k + 1)
        last_max_index = -1
        for i in range(len(nums) - k + 1):
            if last_max_index < i:
                last_max_index = i
                for j in range(i, i + k):
                    if nums[j] > nums[last_max_index]:
                        last_max_index = j
            elif nums[last_max_index] < nums[i + k - 1]:
                last_max_index = i + k - 1
            reuslt[i] = nums[last_max_index]
        return reuslt


