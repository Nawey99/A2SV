# Problem: Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = ListNode(0,head)
        slow = ListNode(0,head)
        while fast and slow and fast.next and fast.next.next and slow.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False