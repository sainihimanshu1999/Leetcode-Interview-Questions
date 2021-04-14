'''
reversing binary bits and then converting them to decimal value or base 2
'''
def reversebits(self,n):
    answer = 0
    for i in range(32):
        answer = answer*2+(n%2)
        n = n//2
    return answer
