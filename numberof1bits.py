'''
it is also knows as hamming wieght problem, a binary number string is given and we have to calculate 
number of 1 bits in that
'''

def calculate(self,n):
    return len([char for char in bin(n) if char == '1'])