# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while slow and fast:
            if not fast.next or not fast.next.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
    
    def detectCycle0(self, head):
        slow = head
        quick = head
        while quick and quick.next:
            quick = quick.next.next
            slow = slow.next
            if quick == slow:
                break
        if quick and quick.next:
            slow = head
            while slow != quick:
                slow = slow.next
                quick = quick.next
            return quick
        return None
