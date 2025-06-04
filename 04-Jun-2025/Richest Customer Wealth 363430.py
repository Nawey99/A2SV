# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        Max= 0 
        for i in accounts:
            x = 0
            for j in i:
                x+=j
            Max = max(Max,x)
        return Max