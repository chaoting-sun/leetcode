class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        if len(self.q1):
            self.q1.append(x)
        else:
            self.q1.append(x)

    def pop(self) -> int:
        if len(self.q1):
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
            return self.q1.popleft()
        else:
            while len(self.q2) > 1:
                self.q1.append(self.q2.popleft())
            return self.q2.popleft()

    def top(self) -> int:
        if len(self.q1):
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
            last = self.q1.pop()
            self.q2.append(last)
            return last
        else:
            while len(self.q2) > 1:
                self.q1.append(self.q2.popleft())
            last = self.q2.pop()
            self.q1.append(last)
            return last

    def empty(self) -> bool:
        return not (len(self.q1) or len(self.q2))
        
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
