# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generateTreeNode(start, end):
            res = []
            if start == end:
                res.append(TreeNode(start))
                return res
            if start > end:
                res.append(None)
                return res

            for i in range(start, end+1):
                left = generateTreeNode(start, i-1)
                right = generateTreeNode(i+1, end)
                for j in left:
                    for k in right:
                        tmp = TreeNode(i)
                        tmp.left = j
                        tmp.right = k
                        res.append(tmp)
            return res

        if n == 0:
            return []
        return generateTreeNode(1, n)

    def generateTrees0(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # T[i, j] = 4 all k: T[i, k-1] + k + T[k+1, j]

        T = [[[TreeNode(x+1)] if x == y else []
              for y in range(n)] for x in range(n)]
        if n == 0:
            return []
        for length in range(1, n):
            for i in range(n-length):
                j = i + length
                for k in range(i, j+1):
                    if k == i:
                        ll = [None]
                    else:
                        ll = T[i][k-1]
                    if k == j:
                        rl = [None]
                    else:
                        rl = T[k+1][j]
                    for ln in ll:
                        for rn in rl:
                            t = TreeNode(k+1)
                            t.left = ln
                            t.right = rn
                            T[i][j].append(t)
        return T[0][n-1]
