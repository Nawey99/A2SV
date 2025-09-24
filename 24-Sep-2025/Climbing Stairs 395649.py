# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        fib = 1
        fib1 = 2
        if n==1:
            return fib
        for i in range(2, n):
            temp = fib1
            fib1 = fib +fib1
            fib = temp
        return fib1