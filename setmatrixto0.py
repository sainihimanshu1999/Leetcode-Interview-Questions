class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        m=len(matrix)
        n=len(matrix[0])
        rl=[]
        cl=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rl.append(i)
                    cl.append(j)

        rs=list(set(rl))
        cs=list(set(cl))
        while len(rs)>0:
            row=rs.pop()
            for j in range(n):
                matrix[row][j]=0

        while len(cs)>0:
            col=cs.pop()
            for i in range(m):
                matrix[i][col]=0
                
        return matrix


