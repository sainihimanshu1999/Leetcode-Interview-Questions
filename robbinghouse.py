'''
It is a very simple dp solution
'''

def rob(self,nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    nums[1] = max(nums[0],nums[1])

    for i in range(2,n):
        nums[i] = max(nums[i-1],nums[i-2]+nums[i])
    return nums[n-1]