'''
we have use heapq in this
'''
from heapq import heappush,heappop
class Solution:
    def skyline(self,buildings):
        events = [(L,-H,R) for L,R,H in buildings]
        events += list((R,0,0) for _ ,R, _ in buildings)
        events.sort()

        res = [[0,0]]
        live = [(0,float('inf'))]

        for pos,negH,R in events:
            while live[0][1]<=pos:
                heappop(live)
            if negH:
                heappush(live, (negH,R))

            if res[-1][1] != -live[0][0]:
                res += [[pos, -live[0][0]]]
        return res[1:]