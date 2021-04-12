class Solution:
    def canCompleteCiruit(self,gas,cost):
        if len(gas)==0 or len(cost) == 0 or sum(gas)<sum(cost):
            return -1

        index = 0
        leftgas = 0
        for i in range(len(gas)):
            leftgas += gas[i]-cost[i]
            if leftgas<0:
                leftgas = 0
                index = i+1
        return index