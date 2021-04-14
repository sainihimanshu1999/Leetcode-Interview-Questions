def reverselinked(self,head):
    curr = head
    prev = None
    new = curr.next
    while curr:
        new = curr.next
        curr.next = prev
        prev = curr
        curr = new
    head = prev
    return head