from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groupedWords = defaultdict(list)
        
        for word in strs:
            groupedWords[''.join(sorted(word))].append(word)
            
        return groupedWords.values()