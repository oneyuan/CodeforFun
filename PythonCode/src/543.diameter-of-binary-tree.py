#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1

        def maxLenth(root):
            if not root:
                return 0
            L = maxLenth(root.left)
            R = maxLenth(root.right)
            self.ans = max(self.ans, L + R)
            return 1 + max(L, R)

        if not root or (not root.left and not root.right):
            return 0
        maxLenth(root)
        return self.ans


