class MyQueue:

    def __init__(self):
        self.stk1, self.stk2 = [], []

    def _move(self, s_from, s_to):
        while len(s_from):
            s_to.append(s_from.pop())

    def push(self, x: int) -> None:
        print('push')
        if not len(self.stk1):
            self._move(self.stk2, self.stk1)
        self.stk1.append(x)

    def pop(self) -> int:
        if not len(self.stk2):
            self._move(self.stk1, self.stk2)
        return self.stk2.pop()

    def peek(self) -> int:
        if not len(self.stk2):
            self._move(self.stk1, self.stk2)
        return self.stk2[-1]

    def empty(self) -> bool:
        return not (len(self.stk1) or len(self.stk2))


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()