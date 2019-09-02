#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
import collections

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = collections.defaultdict(lambda: Node(0, None, None))
        dic[None] = None
        n = head
        while n:
            dic[n].val = n.val
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next
        return dic[head]

    def copyRandomList0(self, head: 'Node') -> 'Node':
        if not head:
            return None
        hashMap = {}
        newHead = Node(head.val, None, None)
        hashMap[head] = newHead

        u, v = head, newHead
        while u:
            v.random = u.random
            if u.next:
                v.next = Node(u.next.val, None, None)
                hashMap[u.next] = v.next
            else:
                v.next = None
            u = u.next
            v = v.next

        node = newHead
        while node:
            if node.random:
                node.random = hashMap[node.random]
            node = node.next

        return newHead
