# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        while low<=high:
            m = (low+high)//2
            if isBadVersion(m):
                high = m-1
            else:
                low = m+1
        return low