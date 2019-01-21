class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution:
    def addTwoNumbers_1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = tmp = ListNode(0)
        n1 = l1
        n2 = l2
        q = 0
        while n1 or n2 or q:
            if n1:
                r1 = n1.val
                n1 = n1.next
            else:
                r1 = 0
            if n2:
                r2 = n2.val
                n2 = n2.next
            else:
                r2 = 0
            t1 = r1 + r2 + q
            t = t1 % 10
            q = t1 // 10
            tmp.next = ListNode(t)
            tmp = tmp.next
        return res.next
    
    def addTwoNumbers0(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0
        ret = ListNode(0)
        cur = ret
        while l1 and l2:
            cur.next = ListNode((l1.val + l2.val + c) % 10)
            cur = cur.next
            c = (l1.val + l2.val + c)  // 10
            l1 = l1.next
            l2 = l2.next
        while l1:
            cur.next = ListNode((l1.val + c) % 10)
            cur = cur.next
            c = (l1.val + c)  // 10
            l1 = l1.next
        while l2:
            cur.next = ListNode((l2.val + c) % 10)
            cur = cur.next
            c = (l2.val + c)  // 10
            l2 = l2.next
        if c:
            cur.next = ListNode(c)
            cur = cur.next
        return ret.next
    