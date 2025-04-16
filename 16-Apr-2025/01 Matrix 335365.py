# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        height = [[-1]*m for i in range(n)]
        que =deque()
        def inbound(i,j):
            return -1<j<m and -1<i<n
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    que.append((i,j))
                    height[i][j] = 0
        while que:
            i, j = que.popleft()
            for dx, dy in dir:
                ni, nj = i + dx, j + dy
                if inbound(ni,nj) and height[ni][nj] == -1:
                    height[ni][nj] = height[i][j] + 1
                    que.append((ni, nj))
                    
        return height