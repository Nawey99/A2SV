# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class Node:
    def __init__(self,val=0,Next=None,Prev=None):
        self.Next = Next
        self.Prev = Prev
        self.val = val
class MyCircularDeque:

    def __init__(self, k: int):
        self.Limit = k
        self.Len = 0
        self.Head = None
        self.Tail = None

    def insertFront(self, value: int) -> bool:
        if self.Len<self.Limit:
            temp = Node(value)
            if self.Len == 0:
                self.Head = self.Tail = temp
                temp.Next = temp.Prev = temp
            else:
                temp.Next = self.Head
                temp.Prev = self.Tail
                self.Head.Prev = temp
                self.Head = temp
                self.Tail.Next = temp
            self.Len +=1
            return True
        else:
            return False
            
    def insertLast(self, value: int) -> bool:
        if self.Len<self.Limit:
            temp = Node(value)
            if self.Len == 0:
                self.Head = self.Tail = temp
                temp.Next = temp.Prev = temp
            else:
                temp.Next = self.Head
                temp.Prev = self.Tail
                self.Head.Prev = temp
                self.Tail.Next = temp
                self.Tail=temp
            self.Len +=1
            return True
        else:
            return False
    def deleteFront(self) -> bool:
        if self.Len <= 0:
            return False
        else:
            if self.Len==1:
                self.Head= None
                self.Tail = None
                self.Len = 0
            else:
                self.Head = self.Head.Next
                self.Tail.Next = self.Head
                self.Head.Prev = self.Tail
                self.Len -=1
        return True


    def deleteLast(self) -> bool:
        if self.Len <= 0:
            return False
        else:
            if self.Len==1:
                self.Head= None
                self.Tail = None
                self.Len = 0
            else:
                self.Tail = self.Tail.Prev
                self.Head.Prev = self.Tail
                self.Tail.Next = self.Head
                self.Len -=1
        return True

    def getFront(self) -> int:
        if self.Len == 0:
            return -1
        return self.Head.val
        
    def getRear(self) -> int:
        if self.Len == 0:
            return -1
        return self.Tail.val

    def isEmpty(self) -> bool:
        return self.Len == 0

    def isFull(self) -> bool:
        return self.Len == self.Limit
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()