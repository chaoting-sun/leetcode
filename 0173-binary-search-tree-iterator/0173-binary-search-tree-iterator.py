# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.id = -1
        self.val_in_order = []
        self.in_order_traversal(root)

    def in_order_traversal(self, root):
        if root.left:
            self.in_order_traversal(root.left)
        self.val_in_order.append(root.val)
        if root.right:
            self.in_order_traversal(root.right)

    def next(self) -> int:
        self.id += 1
        return self.val_in_order[self.id]

    def hasNext(self) -> bool:
        return self.id + 1 < len(self.val_in_order)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()