# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        col = len(matrix[0])
        row = len(matrix)
        self.prefix =[[0]*(col+1) for _ in range(row+1)]
        for i in range(1,row+1):
            for j in range(1,col+1):
                up = self.prefix[i-1][j]
                left = self.prefix[i][j-1]
                dig = self.prefix[i-1][j-1]
                self.prefix[i][j]=up+left-dig+matrix[i-1][j-1]
    
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1,r2,c1,c2=r1+1,r2+1,c1+1,c2+1
        dig = self.prefix[r1-1][c1-1]
        up = self.prefix[r1-1][c2]
        left = self.prefix[r2][c1-1]
        ans = self.prefix[r2][c2]
        print(ans,up,left,dig)
        return ans+dig-up-left



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
