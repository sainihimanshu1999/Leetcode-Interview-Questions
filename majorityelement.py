def majority(self,nums):
    dic = {}
    n = len(nums)
    for i in nums:
        dic[i] = dic.get(i,0)+1

    for key, val in dic.items():
        if val == n/2 :
            return key