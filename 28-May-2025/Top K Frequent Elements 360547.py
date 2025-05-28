# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = []
        store =[]
        for key,val in count.items():
            heappush(store,[-val,key])
        for _ in range(k):
            x = heappop(store)
            ans.append(x[1])
        return ans