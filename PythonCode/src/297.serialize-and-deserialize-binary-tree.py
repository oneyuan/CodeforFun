#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (41.26%)
# Likes:    1545
# Dislikes: 75
# Total Accepted:    190K
# Total Submissions: 460.6K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
# 
# Example: 
# 
# 
# You may serialize the following tree:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠    / \
# ⁠   4   5
# 
# as "[1,2,3,null,null,4,5]"
# 
# 
# Clarification: The above format is the same as how LeetCode serializes a
# binary tree. You do not necessarily need to follow this format, so please be
# creative and come up with different approaches yourself.
# 
# Note: Do not use class member/global/static variables to store states. Your
# serialize and deserialize algorithms should be stateless.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serializedTree = []
        def helpSerialize(root):
            if not root:
                serializedTree.append('*')
            else:
                serializedTree.append(root.val)
                helpSerialize(root.left)
                helpSerialize(root.right)
        helpSerialize(root)
        return serializedTree

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helpDeserialize():
            node = next(iteration)
            if node == "*":
                return None
            tNode = TreeNode(node)
            tNode.left = helpDeserialize()
            tNode.right = helpDeserialize()
            return tNode
        iteration = iter(data)
        return helpDeserialize()

    def serialize0(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            result.append(str(node.val) if node else "null")
            if node:
                queue.append(node.left)
                queue.append(node.right)

        while result and result[-1] == 'null':
            result.pop()

        return ','.join(result)

    def deserialize0(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def create_node(i):
            if i >= len(data) or data[i] == 'null' or data[i] == '':
                return None
            node = TreeNode(data[i] if data[i] != '' else '')
            node.left = create_node(2 * i + 1)
            node.right = create_node(2 * i + 2)
            return node

        data = data.split()
        root = create_node(0)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

