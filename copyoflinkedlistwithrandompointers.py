'''
Deep copy of linked list having both next and randon pointer
'''

class Solution:
    def solve(self,head):
        x = collections.defaultdict(lamba: Node(0))
        x[None] = None
        temp = head
        while temp:
            x[temp].val = temp.val
            x[temp].next = x[temp.next]
            x[temp].random = x[temp.random]
            temp = temp.next
        return x[head]