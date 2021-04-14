def duplicates(self,nums):
    dic = set()
    for i in nums:
        if i in dic:
            return True
        else:
            dic.add(i)
    return False


'''
One more concise way
'''
def duplicates(self,nums):
    return len(nums) != len(set(nums))