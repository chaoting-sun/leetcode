### method1: stack + heap

# class Node:
#     def __init__(self, val, exist=True):
#         self.val = val
#         self.exist = exist
#     def __lt__(self, other):
#         return self.val < other.val
        

# class MinStack:
#     def __init__(self):
#         self.stk = []
#         self.minheap = []

#     def push(self, val: int) -> None:
#         node = Node(val)
#         self.stk.append(node)
#         heapq.heappush(self.minheap, node)       

#     def pop(self) -> None:
#         node = self.stk.pop()
#         node.exist = False
        
#     def top(self) -> int:
#         return self.stk[-1].val

#     def getMin(self) -> int:
#         while not self.minheap[0].exist:
#             heapq.heappop(self.minheap)
#         return self.minheap[0].val
        

### method2: 2 stacks

class MinStack:
    def __init__(self):
        self.stk = []
        self.minStk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.minStk or self.minStk[-1] >= val:
            self.minStk.append(val)

    def pop(self) -> None:
        if self.minStk[-1] == self.stk.pop():
            self.minStk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minStk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()