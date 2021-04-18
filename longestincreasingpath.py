def longestincreasingpath(self,matrix):
    if not matrix or not matrix[0]:
        return None

    m,n = len(matrix),len(matrix[0])

    dp = [[0]*n for _ in range(m)]

    def dfs(i,j):
        if not dp[i][j]:
            val = matrix[i][j]

        #up
        if i and val>matrix[i-1][j]:
            up = dfs(i-1,j)
        else:
            up = 0

        #down
        if i<m-1 and val>matrix[i+1][j]:
            down = dfs(i+1,j)
        else:
            down = 0

        #left

        if j and val>matrix[i][j-1]:
            left = dfs(i,j-1)
        else:
            left = 0

        #right

        if j<n-1 and val>matrix[i][j+1]:
            right = dfs(i,j+1)
        else:
            right = 0

        dp[i][j] = 1 + max(up,down,right,left)
        return dp[i][j]
    result = []
    for x in range(m):
        for y in range(n):
            result.append(dfs(x,y))
    
    return max(result)