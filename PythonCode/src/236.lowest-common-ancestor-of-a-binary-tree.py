#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (35.12%)
# Total Accepted:    250.4K
# Total Submissions: 702.8K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”
# 
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
# 
# Example 2:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.
# 
# 
# 
# 
# Note:
# 
# 
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverseTree(cur):
            if not cur:
                return False
            left = traverseTree(cur.left)
            right = traverseTree(cur.right)
            mid = cur == p or cur == q
            if mid + left + right >= 2:
                self.ans = cur
            return mid or left or right
        
        traverseTree(root)
        return self.ans

    def __init__(self):
        self.memo = {}

    def isChild(self, root, node):
        if (root, node) in self.memo:
            return self.memo[(root, node)]
        if root is None:
            return False
        if root == node:
            return True
        ret = self.isChild(root.left, node) or self.isChild(root.right, node)
        self.memo[(root, node)] = ret
        return ret

    def lowestCommonAncestor0(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if (root == p or root == q):
            return root

        if self.isChild(p, q):
            return p
        if self.isChild(q, p):
            return q

        def helper(root, p, q):
            pIsLeft = self.isChild(root.left, p)
            qIsRight = self.isChild(root.right, q)

            if (pIsLeft and qIsRight) or (not pIsLeft and not qIsRight):
                return root

            if (pIsLeft):
                return self.lowestCommonAncestor(root.left, p, q)
            return self.lowestCommonAncestor(root.right, p, q)

        return helper(root, p, q)
