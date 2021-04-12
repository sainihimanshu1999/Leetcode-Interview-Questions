class Solution:
    def lenght(self,A):
        A = set(A)
        best = 0
        for x in A:
            if x-1 not in A:
                y = x+1
                while y in A:
                    y += 1
                best = max(best,y-x)
        return best