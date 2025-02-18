# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        count = 0
        rs = 0
        for i in nums:
            rs +=i
            count += dic[rs-k]
            dic[rs] += 1
        return count
