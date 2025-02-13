# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, peo: List[int], limit: int) -> int:
        peo.sort()
        l = 0
        r = len(peo)-1
        count = 0
        while l<=r:
            if peo[l] + peo[r]  <= limit:
                l += 1
            r -= 1
            count += 1
        return count
