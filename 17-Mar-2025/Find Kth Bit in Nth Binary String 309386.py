# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def ans(self,n,k):
        xx = pow(2,n)
        h = xx//2
        if n == 1:
            return 0
        if k == h:
            return 1
        if k > h:
            y = h-(k-h)
            return 1-self.ans(n-1,y)
        if k < h:
            return self.ans(n-1,k)
    def findKthBit(self, n: int, k: int) -> str:
        ans = str(self.ans(n,k))
        return ans