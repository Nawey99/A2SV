# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        w = [float('inf')] * (amount+1)
        w[0] = 0
        for i in range(1,amount+1):
            for j in coins:
                if i-j >-1:
                    w[i] = min(w[i],1+w[i-j])
        x =  w[amount]
        return -1 if x == float('inf') else x

        