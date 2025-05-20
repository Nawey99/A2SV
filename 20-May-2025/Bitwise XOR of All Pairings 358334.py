# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        n,m = len(nums1),len(nums2)
        if n&1:
            for i in nums2:
                ans ^= i
        if m&1:
            for i in nums1:
                ans^=i
        return ans