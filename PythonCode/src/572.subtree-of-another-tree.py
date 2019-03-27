#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (41.19%)
# Total Accepted:    92K
# Total Submissions: 222.2K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
#
# Given two non-empty binary trees s and t, check whether tree t has exactly
# the same structure and node values with a subtree of s. A subtree of s is a
# tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.
#
#
# Example 1:
#
# Given tree s:
#
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
#
# Given tree t:
#
# ⁠  4
# ⁠ / \
# ⁠1   2
#
# Return true, because t has the same structure and node values with a subtree
# of s.
#
#
# Example 2:
#
# Given tree s:
#
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
#
# Given tree t:
#
# ⁠  4
# ⁠ / \
# ⁠1   2
#
# Return false.
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def subset(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val == t.val:
                return subset(s.left, t.left) and subset(s.right, t.right)
            return False

        if not s and not t:
            return True
        if not s or not t:
            return False
        left = False
        right = False
        l1 = False
        r1 = False
        if s.val == t.val:
            l1 = subset(s.left, t.left)
            r1 = subset(s.right, t.right)
            if l1 and r1:
                return True
        left = self.isSubtree(s.left, t)
        right = self.isSubtree(s.right, t)
        return left or right

    def isSubtree0(self, s, t):
        def compare(s, t, checkEqual):
            if not s and not t:
                return True
            if not s or not t:
                return False

            if s.val != t.val:
                if checkEqual:
                    return False
                else:
                    return compare(s.left, t, False) or compare(s.right, t, False)
            else:
                return (compare(s.left, t.left, True) and compare(s.right, t.right, True)) or \
                                    compare(s.left, t, False) or compare(
                                        s.right, t, False)

        return compare(s, t, False)

