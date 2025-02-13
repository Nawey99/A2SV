# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        x = int(sqrt(c))
        l = 0
        while l <= x:
            y = (l) **2
            z = (x) **2
            if z+y > c:
                x -=1
            elif z+y < c:
                l +=1
            elif z+y == c:
                return True
        return False