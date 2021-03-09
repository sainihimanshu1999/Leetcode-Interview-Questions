def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = []
        first = -1
        last = -1
        for i in range(len(nums)):
            if(target!=nums[i]):
                continue
            if first == -1:
                first = i
            last = i
            
        if first !=-1:
            a.append(first)
            a.append(last)
            return a
        else:
            a.append(-1)
            a.append(-1)
            return a
            