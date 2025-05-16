# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        left = bin(left)[2::]
        right = bin(right)[2::]
        r= len(right)
        l = len(left)
        left = ("0" * (r-l)) +left
        ans =''
        for i in range(r):
            if left[i] == right[i]:
                ans += left[i]
            else:
                ans += '0' * (r-(i))
                break
        return int(ans,2)