# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        n,m = len(board), len(board[0])
        def inbound(x,k):
            return -1 < x < n and -1 < k < m
        dimentions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(i,j):
            if not inbound(i,j):
                return 
            if board[i][j] != 'O':
                return
            board[i][j] = 'P'
            for row,col in dimentions:
                new_row = i + row
                new_col = j + col
                dfs(new_row,new_col)

        for i in range(m):
            if board[0][i] == 'O':
                dfs(0,i)
            if board[n-1][i] == 'O':
                dfs(n-1,i)
        for i in range(n):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][m-1] == 'O':
                dfs(i,m-1)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'P':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        
       