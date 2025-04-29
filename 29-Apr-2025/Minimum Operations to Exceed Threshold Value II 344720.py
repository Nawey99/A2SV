# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)  
        steps = 0

        while nums and nums[0] < k:
            if len(nums) < 2:
                return -1  

            Min1 = heapq.heappop(nums)
            Min2 = heapq.heappop(nums)

            new_val = Min1 * 2 + Min2
            heapq.heappush(nums, new_val)

            steps += 1

        return steps