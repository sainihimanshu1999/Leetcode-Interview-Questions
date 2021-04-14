def kthlargest(self,nums):
    nums = sorted(nums)
    for i in range(k):
        x = nums.pop()
    return x

'''
One More
'''
def kthlargest(self,nums):
    nums = sorted(nums)
    n = len(nums)
    return nums[n-k]
