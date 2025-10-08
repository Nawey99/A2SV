# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        memo = {(True,n):0 , (False,n):0}
        for idx in range(len(prices)-1,-1,-1):
            for canbuy in range(2):
                if canbuy:
                    memo[(canbuy,idx)]= max(memo[(not canbuy,idx+1)]-prices[idx]-fee,memo[(canbuy,idx+1)])
                else:
                    memo[(canbuy,idx)]= max(prices[idx]+memo[(not canbuy,idx+1)],memo[(canbuy,idx+1)])   

        # def dp(canbuy,idx):
        #     if idx == len(prices):
        #         return 0
        #     if (canbuy,idx) not in memo:
        #         if canbuy:
        #             memo[(canbuy,idx)]= max(dp(not canbuy,idx+1)-prices[idx]-fee,dp(canbuy,idx+1))
        #         else:
        #             memo[(canbuy,idx)]= max(prices[idx]+dp(not canbuy,idx+1),dp(canbuy,idx+1))
        #     return memo[(canbuy,idx)]
        return memo[(True,0)]