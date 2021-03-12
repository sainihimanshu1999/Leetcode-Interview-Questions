class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        x,y = 1,1
        for i in range(n):
            x,y = y,x+y
        return x