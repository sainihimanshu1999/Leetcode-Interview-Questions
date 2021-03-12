class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        intervals.sort()
        
        interval = intervals[0]
        
        for i in range(1,len(intervals)):
            newInterval = intervals[i]
            if interval[1]>=newInterval[0]:
                interval = [interval[0],max(interval[1],newInterval[1])]
            else:
                result.append(interval)
                interval = newInterval
                
        result.append(interval)
        return result