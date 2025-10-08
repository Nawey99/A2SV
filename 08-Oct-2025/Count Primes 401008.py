# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        ans = [True] * n
        count = 0
        for i in range(2,n):
            if ans[i-2]:
                count +=1
                temp = i
                while temp <=n:
                    ans[temp-2] = False
                    temp +=i
        return count
