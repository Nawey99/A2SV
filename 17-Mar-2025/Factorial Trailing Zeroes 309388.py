# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def fac(self, n:int):
        if n == 0:
            return 1
        return n * self.fac(n-1)
    def trailingZeroes(self, n: int) -> int:
        x = self.fac(n)
        count =0
        while x> 0:
            if x % 10 == 0:
                count +=1
                x //=10
            else:
                break
        return count