"""
Method 1: 2 queues

Time:
    push: O(1)
    pop: O(n)
    top: O(n)
    empty: O(1)
Space: O(n)
"""

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def _get_queues(self):
        return (self.q1, self.q2) if self.q1 else (self.q2, self.q1)

    def push(self, x: int) -> None:
        active_q, _ = self._get_queues()
        active_q.append(x)

    def pop(self) -> int:
        active_q, backup_q = self._get_queues()
        while len(active_q) > 1:
            backup_q.append(active_q.popleft())
        return active_q.popleft()

    def top(self) -> int:
        active_q, backup_q = self._get_queues()
        while len(active_q) > 1:
            backup_q.append(active_q.popleft())
        last = active_q.popleft()
        backup_q.append(last)
        return last

    def empty(self) -> bool:
        return not (len(self.q1) or len(self.q2))

"""
Method 2: 1 queue

Time:
    push: O(1)
    pop: O(n)
    top: O(n)
    empty: O(1)
Space: O(n)
"""

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        n = len(self.q)
        for i in range(n-1):
            self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        n = len(self.q)
        for i in range(n-1):
            self.q.append(self.q.popleft())
        last = self.q.popleft()
        self.q.append(last)
        return last

    def empty(self) -> bool:
        return not self.q

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
