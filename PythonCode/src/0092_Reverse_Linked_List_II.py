class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        stack = []
        dummy = ListNode(0)
        pre = ListNode(0)
        dummy = pre
        tmp = head
        count = 0
        while tmp:
            count += 1
            if count < m:
                pre.next = ListNode(tmp.val)
                pre = pre.next
            if m <= count <= n:
                stack.append(ListNode(tmp.val))
            if count == n:
                end = tmp.next
            if count == m-1:
                start = tmp.next
            tmp = tmp.next
        while stack:
            pre.next = stack.pop()
            pre = pre.next
        pre.next = end
        return dummy.next
    
    def reverse(self, head, count, n):
        start = None
        iter = head
        while count < n:
            next = iter.next
            iter.next = start
            start = iter
            iter = next
            count = count + 1
        head.next = iter
        return start

    def reverseBetween0(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        listNodeBefore = None
        iter = head
        count = 0
        while count < (m-1):
            count = count + 1
            listNodeBefore = iter
            iter = iter.next
        if listNodeBefore != None:
            Reversed = self.reverse(listNodeBefore.next, count, n)
            listNodeBefore.next = Reversed
        else:
            Reversed = self.reverse(head, count, n)
            return Reversed

        return head
