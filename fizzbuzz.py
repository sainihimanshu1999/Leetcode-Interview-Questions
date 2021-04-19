class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        x  = []
        for i in range(1,A+1):
            if i%15 ==0:
                x.append('FizzBuzz')
                continue
            elif i%3 == 0:
                x.append('Fizz')
                continue
            elif i%5 == 0:
                x.append('Buzz')
                continue
            else:
                x.append(i)
                continue
        return x


'''
Second soltuion
'''

def fizzBuzz(self,n):
    words,nums = ['Fizz','Buzz'],[3,5]
    result = []

    for i in range(1,n+1):
        curr = ''
        for j in range(2):
            if i%nums[j] == 0:
                curr += words[j]
        if not curr:
            result.append(str(i))
        else:
            result.append(curr)
    return result
            
            
