# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        target = 0
        ans = 0
        for i in range(len(costs)):
            target += costs[i]
            if target <= coins:
                ans += 1
            else: 
                break
        return ans
            