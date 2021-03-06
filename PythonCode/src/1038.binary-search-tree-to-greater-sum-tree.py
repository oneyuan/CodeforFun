#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/
#
# algorithms
# Medium (80.44%)
# Likes:    122
# Dislikes: 13
# Total Accepted:    8.1K
# Total Submissions: 10K
# Testcase Example:  '[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'
#
# Given the root of a binary search tree with distinct values, modify it so
# that every node has a new value equal to the sum of the values of the
# original tree that are greater than or equal to node.val.
# 
# As a reminder, a binary search tree is a tree that satisfies these
# constraints:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree is between 1 and 100.
# Each node will have value between 0 and 100.
# The given tree is a binary search tree.
# 
# 
# 
# 
# 
# 
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
    val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        Groot = TreeNode(0)
        if root.right:
            Groot.right = self.bstToGst(root.right)
        Groot.val = self.val = self.val + root.val
        if root.left:
            Groot.left = self.bstToGst(root.left)
        return Groot

    curr_sum = 0
    def helper(self, root):
        if root is None:
            return
        self.helper(root.right)
        self.curr_sum += root.val
        root.val = self.curr_sum
        self.helper(root.left)
        
    def bstToGst0(self, root: TreeNode) -> TreeNode:
        self.helper(root)
        return root

