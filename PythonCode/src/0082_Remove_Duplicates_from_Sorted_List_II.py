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
        tmp = head
        pre = head.val
        t = ListNode(0)
        res = t
        count = 0
        while tmp:
            if tmp.val == pre:
                count += 1
            else:
                if count == 1:
                    t.next = ListNode(pre)
                    t = t.next
                count = 1
                pre = tmp.val
            if not tmp.next and count == 1:
                t.next = ListNode(tmp.val)
            tmp = tmp.next
        return res.next
    
    def deleteDuplicates0(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        h, t = None, None
        
        if head:
            cur = head
            while (cur):
                prev = cur
                count = 1
                while (cur.next and cur.next.val == cur.val):
                    count += 1
                    cur = cur.next
                
                cur = cur.next
                
                if (count == 1):    
                    if (h is None):
                        h = t = prev
                    else:
                        t.next = prev
                        t = prev
                    prev.next = None

        
        return h
            