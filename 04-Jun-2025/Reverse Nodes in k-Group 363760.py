# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev_group = dummy

        def _reverse(head1):
            prev =None
            curr = head1
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        while head:
            count = 0
            current = head
            while count < k and current:
                current = current.next
                count += 1
          
            if count == k:
                k_group_end = head
                for _ in range(k - 1):
                    k_group_end = k_group_end.next
                next_group = k_group_end.next
                k_group_end.next = None
                new_group_head = _reverse(head)
              
                prev_group.next = new_group_head
                head.next = next_group
              
                prev_group = head
                head = next_group
            else:
                break
      
        return dummy.next
        
        


        