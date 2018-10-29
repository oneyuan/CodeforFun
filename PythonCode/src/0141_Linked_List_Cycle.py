# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        two pointer
        """
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while fast:
            if slow == fast:
                return True
            if fast.next:
                slow = slow.next
                fast = fast.next.next
            else:
                return False
        return False
    
    def hasCycle0(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
