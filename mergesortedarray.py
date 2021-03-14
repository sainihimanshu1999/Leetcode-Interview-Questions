class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n ==0:
            return nums1
        
        else:
            for i in nums2:
                nums1[m] = i
                m+= 1
                print m
            return nums1.sort()
        