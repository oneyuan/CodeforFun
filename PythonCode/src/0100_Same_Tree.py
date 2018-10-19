# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def traverse(root, tmp):
            if not root:
                tmp.append(float("inf"))
                return 0
            tmp.append(root.val)
            traverse(root.left, tmp)
            traverse(root.right, tmp)

        tmp1 = []
        tmp2 = []
        traverse(p, tmp1)
        traverse(q, tmp2)
        if tmp1 == tmp2:
            return True
        else:
            return False
    
    def isSameTree0(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if not p and not q:
            return True
        elif (p and not q) or (not p and q):
            return False
        elif p.val != q.val:
            return False
        else:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
