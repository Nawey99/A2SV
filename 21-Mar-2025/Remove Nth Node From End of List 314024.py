# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        first, second = dummy,dummy
        for _ in range(n+1):
            if first:
                first = first.next
        while first:
            second = second.next
            first = first.next
        if second.next:
            second.next = second.next.next
        else:
            second.next = None
        return dummy.next