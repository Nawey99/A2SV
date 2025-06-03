# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        ans =0
        def bst(i):
            return citations[i] >= n - i
        low = 0
        high =n-1
        while low<=high:
            mid = (high+low)//2
            if bst(mid):
                high = mid-1
            else:
                low = mid+1
        return n-low