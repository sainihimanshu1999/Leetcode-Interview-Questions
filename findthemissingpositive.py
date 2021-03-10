def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        if m<1: 
            return 1
        
        if len(nums) == 1:
            return 2 if A[0] == 1 else 1
            
        l = [0]*m
        for i in range(len(nums)):
            if nums[i]>0:
                if l[nums[i]-1] != 1:
                    l[nums[i]-1] = 1
        for i in range(len(l)):
            if l[i] == 0:
                return i+1
        return i+2