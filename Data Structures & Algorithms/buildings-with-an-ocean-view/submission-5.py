class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        arr = []
        maxc = (0,-1)
        
        n = len(heights)
        for i, num in enumerate(heights):
            if num > maxc[0]:
                maxc = (num,i)
        maxi = maxc[1]
        for h in range(maxi, n):
            j = h+1
            while j < n and heights[h] > heights[j]:
                j += 1
            if j == n:
                arr.append(h)
        return arr

            

        
        