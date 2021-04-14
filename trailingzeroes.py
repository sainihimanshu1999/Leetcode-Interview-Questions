'''
number divisivble by 5 gives, number of zeroes
as can be divided by 5, it will have one trailing zero
as can be divided by 5*5, it will have 2 trailing zero, and so on
we can strictly talking about factorials
'''

def trailingZeroes(self,n):
    result = 0
    while n>0:
        n = n//5
        result += n
    return result