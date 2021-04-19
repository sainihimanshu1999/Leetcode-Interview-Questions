'''
First method slightly more time consuming
'''
def solve(self,s):
    dic = {}
    for i in s:
        dic[i] = dic.get(i,0)+1
    
    for k,v in dic.items():
        if v == 1:
            return s.index(k)
    return -1


'''
Second method, better than before
'''

def solve2(self,s):
    dic = {}
    seen = set()
    for index,val in enumerate(s):
        if val not in seen:
            dic[val] = index
            seen.add(val)
        elif val in dic:
            del dic[c]
    return min(dic.values()) if dic else -1