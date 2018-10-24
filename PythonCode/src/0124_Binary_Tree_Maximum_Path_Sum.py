# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def thoughroot(root):
            nonlocal res
            if not root:
                return 0
            left = max(0, thoughroot(root.left))
            right = max(0, thoughroot(root.right))
            res = max(res, left+right+root.val)
            return max(left, right) + root.val

        res = -float("inf")
        thoughroot(root)
        return res

    def maxPathSum0(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dp = [-float('inf')]

        def subTree(node, dp):
            if not node.left and not node.right:
                if dp[0] < node.val:
                    dp[0] = node.val
                return node.val
            elif not node.left and node.right:
                v = max(node.val + subTree(node.right, dp), node.val)
                if dp[0] < v:
                    dp[0] = v
                return v
            elif node.left and not node.right:
                v = max(node.val + subTree(node.left, dp), node.val)
                if dp[0] < v:
                    dp[0] = v
                return v
            else:
                l = subTree(node.left, dp)
                r = subTree(node.right, dp)
                v = max(node.val, node.val + l, node.val + r, node.val + l + r)
                if dp[0] < v:
                    dp[0] = v
                return max(node.val, node.val + l, node.val + r)

        subTree(root, dp)

        return dp[0]
