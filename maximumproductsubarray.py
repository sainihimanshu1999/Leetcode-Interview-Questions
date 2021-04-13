class Solution:
    def maxProduct(self,nums):
        A= nums[::-1]
        for i in range(1,len(A)):
            nums[i] *= nums[i-1] or 1
            A[i] *= A[i-1] or 1
        return max(nums+A) 