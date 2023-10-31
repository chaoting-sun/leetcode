# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
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


### better name revised by chatgpt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            # Base values for nodes without children
            leftSum, leftEndPath = -float('inf'), -float('inf')
            rightSum, rightEndPath = -float('inf'), -float('inf')

            # Recurse if children are present
            if node.left: 
                leftSum, leftEndPath = dfs(node.left)
            if node.right: 
                rightSum, rightEndPath = dfs(node.right)
            
            # Compute the current highest sum
            currentHighSum = max(node.val, 
                                 leftSum, 
                                 rightSum, 
                                 leftEndPath + node.val, 
                                 rightEndPath + node.val, 
                                 leftEndPath + node.val + rightEndPath)
            
            # Compute the optimal end path for current node
            optimalEndPath = node.val
            if max(leftEndPath, rightEndPath) > 0:
                optimalEndPath += max(leftEndPath, rightEndPath)
            
            return currentHighSum, optimalEndPath

        max_sum, _ = dfs(root)
        return max_sum


### better

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def backtrack(node):
            nonlocal res # tells that res is not a local variable

            if not node:
                return 0

            left = max(0, backtrack(node.left))
            right = max(0, backtrack(node.right))
            res = max(res, left+right+node.val)
            return max(left, right) + node.val

        backtrack(root)
        return res