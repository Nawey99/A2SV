# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.arr=[]

    def push(self, x: int) -> None:
        self.arr=self.arr+[x]

    def pop(self) -> int:
        x = self.arr[0]
        self.arr=self.arr[1:]
        return x
    def peek(self) -> int:
        return self.arr[0]

    def empty(self) -> bool:
        return len(self.arr)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()