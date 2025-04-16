# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        height = [[-1]*m for i in range(n)]
        que =deque()
        step = 0
        def inbound(i,j):
            return -1<j<m and -1<i<n
        for i in range(n):
            for j in range(len(isWater[i])):
                if isWater[i][j] == 1:
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