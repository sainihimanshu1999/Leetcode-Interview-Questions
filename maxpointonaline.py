class Solution:
    def solve(self,points):
        def sl(currentPoint, points):
            slopes,duplicate,ans = {},0,0

            x1,y1 = currentPoint
            for point in points:
                x2,y2 = point
                if x1 == x2 and y1 == y2:
                    duplicate += 1
                else:
                    slope = (x2-x1)/(y2-y1) if y2!=y1 else 'inf'
                    count = slopes.get(slope,0) + 1
                    slopes[slope] = count
                    ans = max(ans,count)
            return ans+1+duplicate

        ans = 0
        while points:
            currentPoint = points.pop()
            ans = max(ans, sl(currentPoint,points))
        return ans