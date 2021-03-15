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
            
            
