# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = []
        dummy = head
        while dummy:
            res.append(dummy.val)
            dummy= dummy.next
        n = len(res)
        x = n//2
        Max = 0
        for i in range(x):
            x = res[i] + res[n-i-1]
            Max = max(Max,x)
        return Max
