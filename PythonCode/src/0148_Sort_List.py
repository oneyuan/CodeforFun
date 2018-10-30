# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def merge(l1, l2):
            dummy = ListNode(0)
            tmp = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tmp.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    tmp.next = ListNode(l2.val)
                    l2 = l2.next
                tmp = tmp.next
            if l1:
                tmp.next = l1
            if l2:
                tmp.next = l2
            return dummy.next

        if not head or not head.next:
            return head
        fast = head
        slow = head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return merge(l1, l2)

    def sortList0(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        List = []
        p = head
        while p:
            List.append(p.val)
            p = p.next
        List.sort()

        p = head
        for i in range(len(List)):
            p.val = List[i]
            p = p.next
        return head
