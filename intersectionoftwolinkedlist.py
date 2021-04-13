class Solution:
    def intersection(self,headA,headB):
        temp1,temp2 = headA,headB

        while temp1!=temp2:
            temp1 = temp1.next if temp else headB
            temp2 = temp2.next if temp else headA
        return temp1