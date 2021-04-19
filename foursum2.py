from collections import defaultdict
def foursum(self,A,B,C,D):
    wewe = defaultdict(int)
    result = 0
    for a in A:
        for b in B:
            wewe[a+b] +=1
    
    for c in C:
        for d in D:
            result += wewe[-c-d]

    return result