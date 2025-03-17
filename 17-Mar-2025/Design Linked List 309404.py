# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class node:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next
    def __str__(self):
        arr = [self.val]
        temp = self.next
        while temp:
            arr.append(temp.val)
            temp = temp.next
        return '---->'.join(map(str,arr))
class MyLinkedList:
    def __init__(self):
        self.dummy = node()
        self.size = 0
    def get(self, index: int) -> int:
        curr = self.dummy.next
        x = 0
        if self.size <= index or index < 0:
            return -1
        while x<index and curr:
            curr = curr.next
            x +=1
        return curr.val
    def addAtHead(self, val: int) -> None:
        x = self.dummy
        temp = node(val,x.next)
        self.dummy.next = temp
        self.size +=1

    def addAtTail(self, val: int) -> None:
        curr = self.dummy
        temp = node(val,None)
        while curr.next:
            curr = curr.next
        curr.next = temp
        self.size +=1
    def addAtIndex(self, index: int, val: int) -> None:
        if index >self.size or index < 0:
            return
        curr =self.dummy
        x = 0
        while x< index and curr.next:
            curr = curr.next
            x+=1
        temp = node(val,curr.next)
        curr.next = temp
        self.size +=1

    def deleteAtIndex(self, index: int) -> None:
        if index >=self.size or index<0:
            return
        curr =self.dummy
        x = 0
        while x< index and curr.next:
            curr = curr.next
            x +=1
        if curr.next and curr.next.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        self.size -=1
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)