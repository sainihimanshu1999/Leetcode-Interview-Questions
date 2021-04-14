def islands(self,grid):
    m = len(grid)
    n = len(grid[0])
    count = 0

    visited = [[False]*n for i in range(m)]
    def dfs(i,j,grid):
        if i+1<m and not visited[i+1][j]:
            visited[i+1][j]= True
            if grid[i+1][j] == '1':
                dfs(i+1,j,grid)

        if i-1>=0 and not visited[i-1][j]:
            visited[i-1][j] = True
            if grid[i-1][j] == '1':
                dfs(i-1,j,grid)

        if j+1<m and not visited[i][j+1]:
            visited[i][j+1]= True
            if grid[i][j+1] == '1':
                dfs(i,j+1,grid)
        
        if j-1>=0 and not visited[i][j-1]:
            visited[i][j-1] = True
            if grid[i][j-1] == '1':
                dfs(i,j-1,grid)

    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                if grid[i][j] == '1':
                    count+=1
                    dfs(i,j,grid)
    return count

        


