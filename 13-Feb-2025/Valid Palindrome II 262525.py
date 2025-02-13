# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispal(x):
            return x == x[::-1]
        l = 0 
        r = len(s)-1
        while l<r:
            if s[l] != s[r]:
                return ispal(s[l+1:r+1]) or ispal(s[l:r])
            l += 1
            r -= 1
        return True 