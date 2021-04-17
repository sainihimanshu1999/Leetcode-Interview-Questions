'''
it doesnot have very good time complexity
'''
def powerof3(self,n):
    if n==1:
        return True
    while n>1:
        n = n/3
        if n==1:
            return True

    return False


'''
alternative method
'''

def powerof3(self,n):
    return n>0 and (3**19)%n==0