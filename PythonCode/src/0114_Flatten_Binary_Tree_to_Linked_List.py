# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def traverse(root, l):
            if not root:
                return
            l.append(root)
            traverse(root.left, l)
            traverse(root.right, l)

        l = []
        traverse(root, l)
        tmp = root
        i = 1
        while i < len(l):
            tmp.left = None
            tmp.right = l[i]
            i += 1
            tmp = tmp.right
    
    def flatten0(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            previous, current = None, root
            while current:
                if current.left:
                    previous = current.left
                    while previous.right:
                        previous = previous.right
                    previous.right = current.right
                    current.right = current.left
                    current.left = None
                current = current.right
