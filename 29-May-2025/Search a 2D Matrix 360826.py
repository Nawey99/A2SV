# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left,top = 0,0
        n,m = len(matrix),len(matrix[0])
        right,bottom = m-1,n-1
        while top <= bottom:
            mid = (bottom+top) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                top = mid
                break
            elif matrix[mid][0]>target:
                bottom = mid-1
            else:
                top = mid+1
        if top > bottom:
            return False
        row = matrix[top]
        while left <= right:
            mid = (right+left) // 2
            if row[mid] == target:
                return True
            if row[mid] < target:
                left = mid +1
            else:
                right = mid - 1
        return False