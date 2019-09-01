#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def ListToBST(lis):
            if not lis:
                return None
            n = len(lis)
            mid = n//2
            th = TreeNode(lis[mid])
            th.left = ListToBST(lis[:mid])
            th.right = ListToBST(lis[mid+1:])
            return th

        if not head:
            return None
        lis = [head.val]
        tmp = head.next
        while tmp:
            lis.append(tmp.val)
            tmp = tmp.next
        return ListToBST(lis)


        def __init__(self):
            self.values = []

        def sortedListToBST(self, head: ListNode) -> TreeNode:
            if head is None:
                return None
            temp = head
            while temp is not None:
                self.values.append(temp.val)
                temp = temp.next
            n = len(self.values)
            
            def buildTree(x, y, m):
                if x == y:
                    return TreeNode(self.values[x])
                if x+1 == y:
                    ans1 = TreeNode(self.values[y])
                    ans2 = TreeNode(self.values[x])
                    ans1.left = ans2
                    return ans1
                if x+2 == y:
                    ans = TreeNode(self.values[m])
                    ans1 = TreeNode(self.values[x])
                    ans2 = TreeNode(self.values[y])
                    ans.left, ans.right = ans1, ans2
                    return ans
                ans = TreeNode(self.values[m])
                ans.left = buildTree(x, m-1, (x+m-1)//2)
                ans.right = buildTree(m+1, y, (m+1+y)//2)
                return ans
            res = buildTree(0, n-1, n//2)
            return res
        


