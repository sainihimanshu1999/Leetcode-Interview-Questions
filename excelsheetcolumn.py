def solve(self,title):
    ans = 0
    for i in title:
        ans = ans*26 + ord(i)-ord('A')+1
    return ans
