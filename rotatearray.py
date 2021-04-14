'''
I'm not really sure how this works though
'''

def rotate(self,nums,k):
    nums[:k],nums[k:] = nums[len(nums)-k:],nums[:len(nums)-k]
    return nums