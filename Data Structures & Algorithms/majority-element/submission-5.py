class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # count = 1
        # maxc = 0
        # i = 0
        # while i < len(nums):
        #     if nums[i] == nums[i-1]:
        #         while nums[i] == nums[i-1]:
        #             count += 1
        #             if count > len(nums) / 2:
        #                 return nums[i]
        #             i+= 1
        #     else:
        #         i += 1
        chosen = None
        count = 0
        for num in nums:
            if count == 0:
                chosen = num
            if num == chosen:
                count += 1
            else:
                count -= 1
        return chosen