#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        cur = root
        firstInRow = cur.left
        while firstInRow:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = firstInRow
                firstInRow = cur.left
        return root

    def connect0(self, root: 'Node') -> 'Node':
        stack = []
        if not root:
            return root
        root.next = None
        if root.left:
            stack.append(root.left)
        # if root.right:
            stack.append(root.right)
        while stack:
            for _ in range(len(stack)-1):
                node = stack.pop(0)
                node.next = stack[0]
                if node.left:
                    stack.append(node.left)
                # if node.right:
                    stack.append(node.right)
            node = stack.pop(0)
            node.next = None

            if node.left:
                stack.append(node.left)
            # if node.right:
                stack.append(node.right)
        return root


