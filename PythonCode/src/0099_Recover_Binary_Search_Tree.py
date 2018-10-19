# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    first = TreeNode(None)
    second = TreeNode(None)
    pre = TreeNode(-float("inf"))

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def traverse(root):
            if not root:
                return 0
            traverse(root.left)
            if not self.first.val and self.pre.val >= root.val:
                self.first = self.pre
            if self.first.val and self.pre.val >= root.val:
                self.second = root
            self.pre = root
            traverse(root.right)

        traverse(root)
        print(self.first.val, self.second.val)
        self.first.val, self.second.val = self.second.val, self.first.val
    
    def recoverTree0(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.

        morris transversal with constant space
        """
        prev, first, second = None, None, None

        curr = root
        while curr:
        	if prev and prev.val >= curr.val:
        		if not first:
        			first = prev
        		second = curr

        	if curr.left:  # we need to find the previous node before curr
        		pred = curr.left
        		while pred.right and pred.right != curr:
        			pred = pred.right

        		if pred.right != curr:  # we find the previous node of curr
        			pred.right = curr
        			curr = curr.left

        		else:  # we have been here before
        			pred.right = None
        			prev = curr
        			curr = curr.right
        	else:  # if no left child, go to right child
        		prev = curr
        		curr = curr.right

        first.val, second.val = second.val, first.val
