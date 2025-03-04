# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        ans = ''
        n = len(s)
        for i in s:
            if i == '1':
                count +=1
        if count >1:
            ans = '1'
            for i in range(count-2):
                ans += '1'
        for i in range(n-count):
            ans += '0'
        return ans+'1'