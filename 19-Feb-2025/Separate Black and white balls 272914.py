# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        n= len(s)
        s = list(s)
        r = n-1
        count = 0
        l = n-1
        while r>=l>=0:
            if s[r] =='0' and s[l] =='1':
                s[r],s[l]=s[l],s[r]
                count +=r-l
            if s[r] =='1' and r>0:
                r -=1
            l-=1
        return count