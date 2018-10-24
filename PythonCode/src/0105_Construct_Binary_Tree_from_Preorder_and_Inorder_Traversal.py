# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder:
            root = TreeNode(preorder[0])
        else:
            return None
        rootIndex = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:rootIndex+1], inorder[:rootIndex])
        root.right = self.buildTree(preorder[rootIndex+1:], inorder[rootIndex+1:])
        return root
    
    def buildTree0(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return

        root = TreeNode(preorder[0])
        stack = [root]
        i = 0

        for val in preorder[1:]:
            parent = stack[-1]

            if parent.val != inorder[i]:
                parent.left = TreeNode(val)
                stack.append(parent.left)

            else:
                while stack and stack[-1].val == inorder[i]:
                    parent = stack.pop()
                    i += 1
                parent.right = TreeNode(val)
                stack.append(parent.right)

        return root
