# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_head = ListNode(0)
        larger_head = ListNode(0)
        smaller = smaller_head
        larger = larger_head
        while head:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
            else:
                larger.next = head
                larger = larger.next
            head = head.next
            
        larger.next = None
        smaller.next = larger_head.next
        return smaller_head.next