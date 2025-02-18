# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        count1= Counter(s1)
        check = []
        l = 0
        r = len(s1)
        n2 = len(s2)
        while r <= n2:
            count2 = Counter(s2[l:r])
            if count2 == count1:
                return True
            r +=1
            l +=1
        return False
