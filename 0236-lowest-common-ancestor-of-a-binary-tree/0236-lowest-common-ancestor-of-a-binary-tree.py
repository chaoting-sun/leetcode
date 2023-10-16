# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root

        leftRes = rightRes = None
        if root.left: leftRes = self.lowestCommonAncestor(root.left, p, q)
        if root.right: rightRes = self.lowestCommonAncestor(root.right, p, q)

        if leftRes and rightRes: return root
        else: return leftRes or rightRes