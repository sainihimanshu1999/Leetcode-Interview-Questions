'''
This solution is insipired by increasing triplet subsequence, Time complexity O(m*n)
'''

def longestincreasing(self,nums):
    sub = []
    for value in nums:
        pos = 0
        sub_len = len(sub)

        while pos <= sub_len:
            if pos==sub_len:
                sub.append(value)
                break
            elif value<sub[pos]:
                sub[pos] = value
                break
            else:
                pos += 1
    return len(sub)


    '''
    This solution is based on binary search algorithm time omplexity (Onlogn)
    '''

    def longestincreasing(self,nums):

        def binarysearch(sub,val):
            low,high = 0,len(sub)-1
            mid = (low+high)//2

            while(low<=high):
                if sub[mid]<val:
                    low = mid +1
                elif val<sub[mid]:
                    high = mid-1
                else:
                    return mid
            return low


        sub = []
        for val in nums:
            pos = binarysearch(sub,val)
            if pos == len(sub):
                sub.append(val)
            else:
                sub[pos] = val
        return len(sub)
