def canFinish(self, numcourses, pre):
    graph = [[] for _ in range(numcourses)]
    visited = [[] for _ in range(numcourses)]

    for pair in numcourses:
        x,y = pair
        graph[x].append(y)

    for i in range(numcourses):
        if not self.dfs(graph,visited,i):
            return False
    return True

def dfs(self,graph,visited,i):
    if visited[i] == -1:
        reutrn False
    if visited[i] == 1:
        return True
    visited[i] = -1

    for j in graph[i]:
        if not self.dfs(graph,visited,i):
            return False
    visited[i] = True
    return True