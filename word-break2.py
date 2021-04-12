'''
simple recurssion
'''
class Solution:
    def wordBreak(self,s,wordDict):
        if s == '':
            return [[]]

        ans = []
        for word in wordDict:
            if s[:len(word)]==word:
                if len(s)==len(word):
                    ans.append(word)

                else:
                    suffix = s[word:]
                    temp = self.wordBreak(suffix,wordDict)
                    for t in temp:
                        ans.append(word+' '+t)
        return ans