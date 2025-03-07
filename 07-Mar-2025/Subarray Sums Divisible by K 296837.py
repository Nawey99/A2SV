# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        count = 0
        rs = 0
        for i in nums:
            rs += i
            n = rs % k
            if n in dic:
                count += dic[n]
            dic[n] += 1
        return count
