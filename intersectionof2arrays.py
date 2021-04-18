'''
intersection of two arrays, simple method
'''
def intersectionoftwoarrays(self,nums1,nums2):
    nums1.sort()
    nums2.sort()
    a= 0
    b = 0
    result - []

    while a<len(nums1) and b<len(nums2):
        if nums1[a] == nums2[b]:
            result.append(nums1[a])
            a += 1
            b += 1
        elif nums1[a]<nums2[b]:
            a +=1 
        else:
            b += 1
    return result

'''
intersection of two methods using libraries
'''

from collections import Counter
def intersectionoftwoarrays(self, nums1, nums2):
    c1 = Counter(nums1)
    c2 = Counter(nums2)
    return list((c1&c2).elements)