# push -> directly push to stk1
# pop -> if stk2, then pop stk2; if not, move all elements from stk1 to stk2, then pop

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