class Solution:
    def wordBreak(self,s,wordDict):
        d = {}
        def dp(A):
            if A in d:
                return d[A]

            for word in wordDict:
                if A[:len(word)] == word:
                    if len(A)==len(word):
                        d[s] = True
                        return True
                    else:
                        suffix = A[len(word):]
                        if(dp(suffix)):
                            dp[A] = True
                            return dp[A]
            dp[A] = False
            dp[A]
        return dp[s]