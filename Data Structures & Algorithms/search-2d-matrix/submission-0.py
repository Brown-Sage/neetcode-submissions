class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_1d = [element for row in matrix for element in row]
        
        l = 0
        r = len(matrix_1d)-1
        while l <= r:
            mid = (l+r)//2
            if matrix_1d[mid] == target:
                return True
            elif target < matrix_1d[mid]:
                r = mid-1
            else:
                l = mid+1
            
        return False