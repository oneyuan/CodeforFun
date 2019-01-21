# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        lr = []
        tmp = head
        while tmp:
            lr.append(tmp.val)
            tmp = tmp.next
        ll = lr.copy()
        lr.reverse()
        if ll == lr:
            return True
        else:
            return False
    
    def isPalindrome0(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            tmp = slow.next
            
            slow.next = prev
            prev = slow
            
            slow = tmp
            
        while prev:
            if head.val != prev.val:
                return False
            head, prev = head.next, prev.next
        return True