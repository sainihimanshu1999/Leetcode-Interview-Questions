class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        
        dp[1] = 1 if s[0]!='0' else 0
        
        for i in range(2,len(dp)):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
                
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <=26:
                dp[i] += dp[i-2]
        
        return dp[len(s)]
        