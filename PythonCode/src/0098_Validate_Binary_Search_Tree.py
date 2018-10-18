# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root, less, bigger):
            if not root:
                return True
            if root.val >= less or root.val <= bigger:
                return False
            return (helper(root.left, min(less, root.val), bigger) and helper(root.right, less, max(bigger, root.val)))
        return helper(root, float("inf"), -float("inf"))
    
    def isValidBST0(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True

        return self.isValidHelper(root, float('-inf'), float('inf'))

    def isValidHelper(self, root, mini, maxi):

        if root is None:
            return True

        if mini <= root.val and root.val <= maxi:

            return self.isValidHelper(root.left, mini, root.val - 1) and self.isValidHelper(root.right, root.val + 1, maxi)

        return False
