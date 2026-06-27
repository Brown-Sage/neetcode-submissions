class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        arr = [n-1]
        for i in range(n-1, -1, -1):
            diff = heights[i] - heights[arr[-1]]
            if diff > 0:
                arr.append(i)
        return arr[::-1]