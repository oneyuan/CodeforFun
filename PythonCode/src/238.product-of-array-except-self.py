#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (53.64%)
# Total Accepted:    235K
# Total Submissions: 433.6K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
# 
# Example:
# 
# 
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# 
# 
# Note: Please solve it without division and in O(n).
# 
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
# 
#
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []
        outside = -1
        product = 1
        for i in nums:
            if i == 0:
                if outside != -1:
                    return [0 for _ in range(n)]
                outside = nums.index(i)
            else:
                product *= i
        for i in nums:
            if i != 0 and outside == -1:
                output.append(int(product/i))
            elif i == 0:
                output.append(product)
            else:
                output.append(0)
        return output

    def productExceptSelf0(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0, n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output

