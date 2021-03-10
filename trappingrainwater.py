'''
Approach 1st


time complexity  - O(n^2) 
Space complexity - O(1)
'''


class Solution(object):
    def trap(self, arr):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        n = len(arr)
     
    # For every element of the array 
        for i in range(1, n - 1) : 
         
        # Find the maximum element on its left 
            left = arr[i]; 
            for j in range(i) :
                left = max(left, arr[j]); 
         
        # Find the maximum element on its right 
            right = arr[i]
         
            for j in range(i + 1 , n) : 
                right = max(right, arr[j]);
             
        # Update the maximum water
            res = res + (min(left, right) - arr[i]); 
 
        return res



'''
Approach 2nd

time complexity  - O(n)
space comeplexity - O(n)
'''


def trap(self, arr):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(arr)
        left = [0]*n
 

        right = [0]*n
 

        water = 0
 
    
        left[0] = arr[0]
        for i in range( 1, n):
            left[i] = max(left[i-1], arr[i])
 
    
        right[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i + 1], arr[i]);
 
    
        for i in range(0, n):
            water += min(left[i], right[i]) - arr[i]
 
        return water
