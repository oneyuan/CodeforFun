#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#
# https://leetcode.com/problems/linked-list-random-node/description/
#
# algorithms
# Medium (49.25%)
# Likes:    364
# Dislikes: 108
# Total Accepted:    52.5K
# Total Submissions: 106.7K
# Testcase Example:  '["Solution","getRandom"]\n[[[1,2,3]],[]]'
#
# Given a singly linked list, return a random node's value from the linked
# list. Each node must have the same probability of being chosen.
# 
# Follow up:
# What if the linked list is extremely large and its length is unknown to you?
# Could you solve this efficiently without using extra space?
# 
# 
# Example:
# 
# // Init a singly linked list [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);
# 
# // getRandom() should return either 1, 2, or 3 randomly. Each element should
# have equal probability of returning.
# solution.getRandom();
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random
import collections
import bisect
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        result, node, index = self.head, self.head.next, 1
        while node:
            if random.randint(0,index) == 0:
                result = node
            node = node.next
            index += 1
        return result.val
    
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.dict = collections.defaultdict(int)
        total = 0
        while head:
            self.dict[head.val] += 1
            total += 1
            head = head.next

        self.probmap = {}
        self.prob = []
        pval = 0
        for i, (k, v) in enumerate(self.dict.items()):
            pval += v
            self.prob.append(pval / total)
            self.probmap[i] = k
            

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        rd = random.random()
        idx = bisect.bisect_left(self.prob, rd)
        return self.probmap[idx]
        



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

