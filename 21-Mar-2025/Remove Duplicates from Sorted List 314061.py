# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        res = ListNode(0)
        res_head = res
        sets = set()
        while dummy:
            sets.add(dummy.val)
            dummy = dummy.next
        arr = sorted(sets)
        for i in arr:
            temp = ListNode(i,None)
            res.next = temp
            res = res.next
        return res_head.next