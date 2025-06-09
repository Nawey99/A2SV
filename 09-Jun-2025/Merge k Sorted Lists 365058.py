# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = []
        for node in lists:
            while node:
                heappush(ans,node.val)
                node = node.next
        res = ListNode()
        dummy = res
        while ans:
            temp =ListNode(heappop(ans))
            dummy.next= temp
            dummy = dummy.next
        return res.next