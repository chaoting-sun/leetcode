# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0
        queue = [root]
        
        while len(queue):
            size = len(queue)

            for i in range(size):
                root = queue.pop(0)
                if root.left: queue.append(root.left)
                if root.right: queue.append(root.right)
            level += 1
        return level