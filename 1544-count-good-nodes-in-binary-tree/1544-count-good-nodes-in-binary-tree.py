# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxValue):
            good = 0
            if node.val >= maxValue:
                maxValue = max(node.val, maxValue)
                good = 1

            nLeftGood = nRightGood = 0
            if node.left: nLeftGood = dfs(node.left, maxValue)
            if node.right: nRightGood = dfs(node.right, maxValue)
            
            return nLeftGood + good + nRightGood

        return dfs(root, float('-inf'))