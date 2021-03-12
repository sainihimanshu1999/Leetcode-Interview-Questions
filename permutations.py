class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        ret = []
        
        # go through the number list
        for i in range(len(nums)):
            
            # take out the number from the list
            num_perm = nums[:]
            n = num_perm.pop(i)
            perms = self.permute(num_perm)
            
            for p in perms:
                ret.append([n]+p)
                
        return ret
        