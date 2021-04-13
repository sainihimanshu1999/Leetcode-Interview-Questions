'''
We are using binary search algorithm in this question
'''

class Solution:
    def peakelement(self,num):
        n = len(num)
        left = 0
        right = n-1

        while left<right-1:
            mid = (left+right)/2
            if num[mid]>num[mid+1] and num[mid]>num[mid-1]:
                return mid

            if num[mid]<num[mid+1]:
                left = mid+1
            else:
                right = mid -1
        return left if num[left]>=num[right] else right