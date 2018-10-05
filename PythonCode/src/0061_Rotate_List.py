class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or k == 0 or head.next == None:
            return head
        tmp = head.next
        l = [head]
        while tmp:
            l.append(tmp)
            tmp = tmp.next
        if k >= len(l):
            k = k%len(l)
        if k == 0:
            return head
        l[-k-1].next = None
        l[-1].next = head
        return l[-k]
    
    def rotateRight0(self, head, k):
        if head is None or head.next is None :
            return head
    
        listLen = getlen(head);
        Move = k % listLen
        if Move == 0 :
            return head;
    
        Otail = gettail(head)
        Nhead = getNode(head,listLen - Move)
        Ntail = getNode(head,listLen - Move - 1)

        Otail.next = head;
        Ntail.next = None;
        head = Nhead
        return head

def getNode(head,index):  #索引从0开始
    pre = head;
    while index >= 1 :
        pre = pre.next;
        index = index - 1;
    return pre

def gettail(head):
    pre = head;
    while pre.next :
        pre = pre.next
    return pre


def getlen(head) :
    pre = head;
    length = 0;
    while pre :
        length = length + 1;
        pre = pre.next;
    return length

def showlist(head) :
    pre = head
    while pre :
        print(pre.val,end = ' ')
        pre = pre.next
       
    def rotateRight1(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p = head
        size = 0
        while p:
            size += 1
            p = p.next
        if not size:
            return None
        k %= size
        if not k:
            return head
        tail = head
        for _ in range(size-1):
            tail = tail.next
        
        p, q = head, head.next
        for _ in range(size-k-1):
            p = p.next
            q = q.next
        tail.next = head
        p.next = None
        return q
