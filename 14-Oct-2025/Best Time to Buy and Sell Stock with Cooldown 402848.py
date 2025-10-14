# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(idx,isBuy):
            if idx >= n:
                return 0
            if (idx,isBuy) not in memo:
                if isBuy:
                    memo[(idx,isBuy)] =  max(dp(idx+1,isBuy),prices[idx] + dp(idx+2,not isBuy))
                else:
                    memo[(idx,isBuy)] = max(dp(idx+1,isBuy),(dp(idx+1,not isBuy) - (prices[idx])))
            return memo[(idx,isBuy)]
        n = len(prices)
        return dp(0,False)