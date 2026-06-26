class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        arr = []
        
        for i in range(len(heights)-1):
            j = i+1
            while heights[j] < heights[i] and j < len(heights)-1:
                j += 1
            if j  == len(heights)-1 and heights[i] > heights[j]:
                arr.append(i)
        arr.append(len(heights)-1)
        return arr