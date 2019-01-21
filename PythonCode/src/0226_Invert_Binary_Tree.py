Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        tmp = TreeNode(root.val)
        if root.left:
            tmp.right = self.invertTree(root.left)
        if root.right:
            tmp.left = self.invertTree(root.right)
        return tmp

    def invertTree0(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if root==None:
            return 

        right=self.invertTree(root.right)
        left=self.invertTree(root.left)
        root.left=right
        root.right=left
                    
            
            
        return root