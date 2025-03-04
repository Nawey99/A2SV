# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countr=0
        count=0
        for i in s:
            if i == 'R':
                countr+=1
            else :
                countr-=1
            if countr == 0:
                count+=1
        return count