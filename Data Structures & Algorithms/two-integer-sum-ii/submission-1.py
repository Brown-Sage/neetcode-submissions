class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            combine = numbers[left]+numbers[right]
            if combine == target :
                return [left+1, right+1]
            elif combine < target:
                left += 1
            elif combine > target:
                right -= 1
        return [] 