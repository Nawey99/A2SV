# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0
        n = len(nums)
        Max = 0
        inc = deque()
        dec = deque()
        for idx,num in enumerate(nums):
            while inc and nums[inc[-1]] > num:
                inc.pop()
            inc.append(idx)
            while dec and nums[dec[-1]] <= num:
                dec.pop()
            dec.append(idx)
            while abs(nums[dec[0]]-nums[inc[0]]) > limit:
                l+=1
                if dec[0] < l:
                    dec.popleft()
                if inc[0] <l:
                    inc.popleft()
        
            Max = max(Max,idx-l+1)

        return Max
