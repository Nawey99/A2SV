# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxD: int) -> int:
        x = target
        moves = 0
        while x>1:
            if maxD == 0:
                return moves + (x - 1)
            if x % 2 == 0:
                x //= 2
                maxD -= 1
            else:
                x -= 1
            moves += 1
        return moves