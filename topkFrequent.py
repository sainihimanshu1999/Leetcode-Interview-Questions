def topKFrequent(self,nums,k):
    a = []
    dic = {}
    for i in nums:
        dic[i] = dic.get(i,0)+1
    a = sorted(dic,key = dic.get,reverse=True)
    return (a[:k])