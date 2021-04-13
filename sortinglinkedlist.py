'''
Sorting this linked list using merge sort
'''

def sortList(self,head):
    if not head or not head.next:
        return head
    
    slow = head
    fast = head.next

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    start = slow.next
    slow.next = None
    left,right = self.sortList(head),self.sortList(start)
    return mergeList(left,right)

def mergeList(self,l,r):
    if not l or not r:
        return l or r

    dummy = p = ListNode(0)
    while l and r:
        if l.val<r.val:
            p.next = l
            l = l.next
        
        else:
            p.next = r
            r = r.next
        p = p.next
    p.next = l or r
    return dummy.next

