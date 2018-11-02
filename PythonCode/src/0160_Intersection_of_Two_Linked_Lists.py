# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tmpA = headA
        tmpB = headB
        onceA = True
        onceB = True
        if not tmpA or not tmpB:
            return None
        while tmpA != tmpB:
            tmpA = tmpA.next
            tmpB = tmpB.next
            if not tmpA and onceA:
                tmpA = headB
                onceA = False
            if not tmpB and onceB:
                tmpB = headA
                onceB = False
        if tmpA:
            return tmpA
        else:
            return None
    
    def getIntersectionNode0(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        
        pa = headA
        pb = headB
        while pa is not pb:
            if pa:
                pa = pa.next
            else:
                pa = headB
            
            if pb:
                pb = pb.next
            else:
                pb = headA
                
        return pa