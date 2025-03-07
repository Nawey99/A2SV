# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        replica = ListNode(0) 
        dummy = replica
        temp =head
        while temp:
            curr = ListNode(temp.val)
            dummy.next = curr
            dummy= dummy.next
            temp = temp.next    
        prev =None
        curr = replica
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        while head:
            if head.val != prev.val:
                return False
            head=head.next
            prev = prev.next
        return True