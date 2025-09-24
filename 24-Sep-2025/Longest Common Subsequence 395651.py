# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        check = {}
        def dp(i,j):
            if j >= len(text2) or i >= len(text1):
                return 0
            if text1[i] == text2[j]:
                return 1+ dp(i+1,j+1)
            else:
                if (i,j) not in check:
                    check[(i,j)] = max(dp(i,j+1),dp(i+1,j))
                return check[(i,j)]
        return dp(0,0)
            