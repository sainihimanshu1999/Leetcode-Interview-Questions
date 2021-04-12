class solution:
    def singlenum(self,nums):
        x = {}
        for num in nums:
            x[num] = x.get(num,0) + 1

        for key,value in x.items():
            if value == 1:
                return key