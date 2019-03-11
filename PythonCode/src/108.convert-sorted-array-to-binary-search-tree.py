#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (48.99%)
# Total Accepted:    234.7K
# Total Submissions: 479.1K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted array: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: 'List[int]') -> 'TreeNode':
        if not nums:
            return None

        return self.toBstUtil(nums, 0, len(nums) - 1)

    def toBstUtil(self, nums, low, high):

        if low > high:
            return None

        mid = (low + high) // 2

        node = TreeNode(nums[mid])
        node.left = self.toBstUtil(nums, low, mid - 1)
        node.right = self.toBstUtil(nums, mid + 1, high)

        return node

