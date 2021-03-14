class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = list()
        max_area = 0
        index = 0
        while index<len(heights):
            if (not stack) or (heights[stack[-1]]<=heights[index]):
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                
                area = (heights[top_of_stack] * 
                    ((index - stack[-1] - 1)  
                    if stack else index)) 
                
                max_area = max(area,max_area)
                        
        while stack:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] * 
              ((index - stack[-1] - 1)  
                if stack else index)) 
            max_area = max(area,max_area)
            
        return max_area
        