# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        pre = head.val
        tmp = head.next
        t = ListNode(head.val)
        res = t
        while tmp:
            if tmp.val == pre:
                tmp = tmp.next
            else:
                pre = tmp.val
                t.next = ListNode(tmp.val)
                t = t.next
                tmp = tmp.next
        return res
    
    def deleteDuplicates0(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            runner = cur.next
            while runner and runner.val == cur.val:
                runner = runner.next
            cur.next = runner
            cur = runner
        return head