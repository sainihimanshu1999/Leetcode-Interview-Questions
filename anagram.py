'''
First is by using dictionary
'''
def anagram(self,s,t):
    dic1 , dic2 = {},{}

    for i in s:
        dic1[i] = dic1(i,0)+1
    for i in t:
        dic2[i] = dic2(i,0)+1

    return dic1 == dic2


'''
Second by sorting
'''
def anagram(self,s,t):
    return sorted(s) == sorted(t)