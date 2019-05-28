#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        rootIndex = 0
        for index, i in enumerate(inorder):
            if i == postorder[-1]:
                rootIndex = index
        root.left = self.buildTree(inorder[:rootIndex], postorder[:rootIndex])
        root.right = self.buildTree(
            inorder[rootIndex+1:], postorder[rootIndex:-1])
        return root

    def buildTree0(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(left=0, right=len(inorder)):
            nonlocal i
            if right == left:
                return None

            root = TreeNode(postorder[i])
            idx = idx_map[postorder[i]]
            i -= 1
            root.right = helper(idx + 1, right)
            root.left = helper(left, idx)

            return root
        i = len(inorder)-1
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper()

