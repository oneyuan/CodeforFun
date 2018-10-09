# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less = ListNode(0)
        great = ListNode(0)
        l = less
        g = great
        tmp = head
        while tmp:
            if tmp.val < x:
                less.next = ListNode(tmp.val)
                less = less.next
            else:
                great.next = ListNode(tmp.val)
                great = great.next
            tmp = tmp.next
        less.next = g.next
        return l.next
    
    def partition0(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if(head == None) or (head.next == None):
            return head
            
        minNode = None
        maxNode = None
        minHead = None
        maxHead = None
        
        while(head != None):
            if(head.val < x):
                if(minHead == None):
                    minHead = head
                    minNode = head
                else:
                    minNode.next = head
                    minNode = minNode.next
            else:
                if(maxHead == None):
                    maxHead = head
                    maxNode = head
                else:
                    maxNode.next = head
                    maxNode = maxNode.next
            head = head.next
        
        if(maxNode != None):
            maxNode.next = None
        if(minHead != None):
            minNode.next = maxHead
            head = minHead
        else:
            head = maxHead
        return head
    
    