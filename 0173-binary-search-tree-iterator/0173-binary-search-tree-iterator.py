# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
method 1: array

Time:
    a. constructor: O(n)
    b. next: O(1)
    c. hasNext: O(1)
Space: O(n)
"""

# class BSTIterator:

#     def __init__(self, root: Optional[TreeNode]):
#         self.id = -1
#         self._arr = []
#         self._in_order(root)

#     def _in_order(self, root):
#         if root.left:
#             self._in_order(root.left)
#         self._arr.append(root.val)
#         if root.right:
#             self._in_order(root.right)

#     def next(self) -> int:
#         self.id += 1
#         return self._arr[self.id]

#     def hasNext(self) -> bool:
#         return self.id + 1 < len(self._arr)

"""
method 2: stack

Time:
    a. constructor: O(h), where h is tree height
    b. next: amortized O(1), as there are simply 2 operations (push/pop) for each node
Space: O(h), where h is tree height
"""

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.id = -1
        self._stack = []
        while root:
            self._stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self._stack.pop()
        root = node.right
        while root:
            self._stack.append(root)
            root = root.left
        return node.val

    def hasNext(self) -> bool:
        return len(self._stack)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()