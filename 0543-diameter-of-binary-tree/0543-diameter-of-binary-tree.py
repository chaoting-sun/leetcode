### method: dfs
# to compute the diameter of the tree, we compute the diameters of all subtrees and find the largest
# source: https://leetcode.com/problems/diameter-of-binary-tree/solutions/101132/java-solution-maxdepth/comments/104961
# time complexity: O(N); N is the number of nodes.
# space complexity: O(N) (N recursive calls)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def maxHeight(root):
            if not root: return 0
            leftHeight = maxHeight(root.left)
            rightHeight = maxHeight(root.right)
            self.diameter = max(self.diameter, leftHeight + rightHeight)
            return max(leftHeight, rightHeight) + 1
        maxHeight(root)
        return self.diameter

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            if not root: return 0, 0
            
            leftHeight, leftDiameter = helper(root.left)
            rightHeight, rightDiameter = helper(root.right)

            currentHeight = max(leftHeight, rightHeight) + 1 # leaves -> height = 1
            currentDiameter = max(leftDiameter, rightDiameter, leftHeight+rightHeight)
            
            return currentHeight, currentDiameter

        _, diameter = helper(root)
        return diameter