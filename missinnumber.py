def missingNumber(self,nums):
    output = [-1]*(len(nums)+1)

    for i in nums:
        output[i] = i

    for j in range(len(output)):
        if output[j] == -1:
            return j