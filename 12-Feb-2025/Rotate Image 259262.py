# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n-i-1):
                if i <= j:
                    x = n-i-1
                    y = n-j-1
                    temp1 = matrix[i][j]
                    temp2 = matrix[j][x]
                    temp3 = matrix[x][y]
                    matrix[i][j] = matrix[y][i]
                    matrix[j][x] = temp1
                    matrix[x][y] = temp2
                    matrix[y][i] = temp3
