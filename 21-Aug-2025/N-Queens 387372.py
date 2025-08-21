# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        queen = []

        cols = set()
        diag1 = set()
        diag2 = set()

        def bct(row):
            if row == n:
                ans.append(queen[:])
                return

            for col in range(n):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue

                # place queen
                queen.append((row, col))
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)

                bct(row + 1)

                # backtrack
                queen.pop()
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)

        bct(0)
        res = []
        for i in ans:
            temp = [['.'] * n  for i in range(n)]
            for x,y in i:
                temp[x][y] = 'Q'
            dummy =[]
            for i in range(n):
                x = ''.join(temp[i])
                dummy.append(x)
            res.append(dummy)
        return res