def solve(self,s,k):
    if len(s)<k:
        return 0
    c = min(set(s),key = s.count)
    if s.count(c)>=k:
        return len(s)
    return max(self.solve(t,k) for t in s.split(c))