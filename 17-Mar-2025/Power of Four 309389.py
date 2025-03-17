# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<1:
            return False
        x = str(log(n,4))[-1]
        return x=='0'