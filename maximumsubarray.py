#One way to do it
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        endindex = 0
        currMax = nums[0]
        globalMax = nums[0]
        
        for i in range(1,len(nums)):
            currMax = max(nums[i],nums[i]+currMax)
            
            if(currMax>globalMax):
                globalMax = currMax
                endindex = i
                
        startindex = endindex        
        while(startindex>=0):
            globalMax -= nums[startindex]
            
            if globalMax == 0:
                break
            startindex -= 1
            
        arr = nums[startindex:endindex+1]
        return sum(arr)    

#another way to do it
def maxSubArray(self,nums):
    for i in range(1,lens(nums)):
        if nums[i-1]>0:
            nums[i] += nums[i-1]
    return max(nums)