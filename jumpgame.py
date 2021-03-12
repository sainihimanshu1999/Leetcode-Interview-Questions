class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = len(nums) - 1
        curr = 0
        steps = nums[curr]
        #the loop will continue until 1. goal is reached or 2. steps have been depleted
        while curr<goal and steps>0:
            curr += 1
            
            #after this step would either be less than one because we have increase the curr
            #or they will the current number which we are on currently
            steps = max(steps-1,nums[curr])
            
        return curr == goal