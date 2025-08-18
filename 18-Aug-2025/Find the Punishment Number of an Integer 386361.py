# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        res = 0
        def partion(i,curr,tar,s):
            m = len(s)
            if i == m and curr == tar:
                return True
            for j in range(i,m):
                num = s[i:j+1]
                if partion(j+1,curr + int(num),tar,s):
                    return True
            return False
        for i in range(n+1):
            if partion(0,0,i,str(i*i)):
                res+=i*i
        return res