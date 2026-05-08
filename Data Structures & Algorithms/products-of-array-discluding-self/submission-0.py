class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newnum = []
        
        for i in range(0, len(nums)):
            res = 1
            for j in range(0,len(nums)):
                if(j==i):
                    continue
                else:
                    res = res*nums[j]
            newnum.append(res)
        return newnum