# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursion(self, root, leftMost, rightMost):
        # termination
        if not root:
            return True

        if root.left and not leftMost < root.left.val < root.val:
            return False
        if root.right and not root.val < root.right.val < rightMost:
            return False

        return self.recursion(root.left, leftMost, root.val) \
           and self.recursion(root.right, root.val, rightMost)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recursion(root, -2**32, 2**32)