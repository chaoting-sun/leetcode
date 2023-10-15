# two stacks: use stk1 to push and use stk2 to pop and peek.
# if we want to pop or peek and if stk2 is empty, move all
# elements from stk1 to stk2.

# amortized time complexity: O(1)
# because for each element, at most, they are pushed into stk1,
# popped from stk1, pushed into stk2, and popped from stk2.

class MyQueue:

    def __init__(self):
        self.stk1, self.stk2 = [], []

    def move(self):
        if not self.stk2:
            while self.stk1:
                self.stk2.append(self.stk1.pop())

    def push(self, x: int) -> None:
        self.stk1.append(x)

    def pop(self) -> int:
        self.move()
        return self.stk2.pop()

    def peek(self) -> int:
        self.move()
        return self.stk2[-1]

    def empty(self) -> bool:
        return not (len(self.stk1) or len(self.stk2))


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()