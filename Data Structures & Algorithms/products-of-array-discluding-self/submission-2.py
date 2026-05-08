class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newnum = []
        a = 0
        b = 0
        res = 1
        while( a < len(nums)):
            if b == len(nums):
                a = a+1
                b = 0
                newnum.append(res)
                res = 1
            elif b == a:
                b = b+1
            else:
                res = res*nums[b]
                b = b+1
            
        return newnum
