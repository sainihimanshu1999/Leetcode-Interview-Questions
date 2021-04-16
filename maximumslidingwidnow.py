from collections import deque
def maximumslidingwindow(self,nums,k):
    result = []
    q = deque()
    for i,n in enumerate(nums):
        #to keep the righ most element smaller
        while q and nums[q[-1]]<=n:
            q.pop()

        q += [i]
        #to maintain the size of every new subarray
        while i-q[0] >=k:
            q.popleft()
        #max elemet append
        if i+1>=k:
            result.append(nums[q[0]])
    return result