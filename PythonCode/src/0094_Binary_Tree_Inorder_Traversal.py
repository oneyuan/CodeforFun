# Definition for a binary tree node.
# class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root, res):
            if root != None:
                if root.left != None:
                    helper(root.left, res)
                res.append(root.val)
                if root.right != None:
                    helper(root.right, res)

        res = []
        helper(root, res)
        return res

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        node = []
        cur_node = root

        while stack or cur_node:

            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left

            popnode = stack.pop()
            node.append(popnode.val)
            cur_node = popnode.right
        return node
