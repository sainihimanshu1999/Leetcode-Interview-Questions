class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        k = 0
        m = len(matrix)
        l = 0
        n = len(matrix[0])
        a = []
        
        while(k<m and l<n):
            for i in range(l,n):
                a.append(matrix[k][i])
            k+=1
            
            for i in range(k,m):
                a.append(matrix[i][n-1]) 
            n-=1
            
            if(k<m):
                for i in range(n-1,(l-1),-1):
                    a.append(matrix[m-1][i])
                    
                m-=1
                
            if(l<n):
                for i in range(m-1,k-1,-1):
                    a.append(matrix[i][l])
                l+=1
                
                
        return a