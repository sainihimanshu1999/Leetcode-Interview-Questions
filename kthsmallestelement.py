'''
one way 
'''

def kthelement(self,matrix,k):
    op = []
    for i in matrix:
        for y in i:
            op.append(y)

    op.sort()
    return op[k-1]

'''
second way
'''

def kthelement(self,matrix,k):
    op = []
    for row in matrix:
        op+=row
    return sorted(op)[k-1]