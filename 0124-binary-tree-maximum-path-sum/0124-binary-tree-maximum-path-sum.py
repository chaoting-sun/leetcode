# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # if not root.left and not root.right:
        #     return root.val

        def dfs(root):
            lhs = lpath = rhs = rpath = -10E6

            if root.left: lhs, lpath = dfs(root.left)
            if root.right: rhs, rpath = dfs(root.right)
            
            chs = max(root.val, lhs, rhs, lpath+root.val, rpath+root.val, lpath+root.val+rpath)
            hpath = max(lpath, rpath) # highest path
            cpath = root.val
            if hpath > 0:
                cpath += hpath
            return chs, cpath

        chs, _ = dfs(root)
        return chs