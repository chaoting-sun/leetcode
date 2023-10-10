# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### method1: top down approach

# time complexity: O(N^2)
# space complexity: O(N)

# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         if not root: return True

#         def depth(node):
#             if not node: return 0
#             else: return max(depth(node.left), depth(node.right)) + 1

#         # use the definition of balanced binary tree:
#         # the difference between the depths of the two sub trees
#         # are not bigger than 1, and both of the left sub tree
#         # and right sub tree are also balanced
#         return abs(depth(root.left)-depth(root.right)) <= 1 \
#            and self.isBalanced(root.left) and self.isBalanced(root.right)
            

### method2: down top approach; dfs

class Solution:    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfsHeight(root):
            if not root: return 0

            # check if left sub tree is balanced
            leftHeight = dfsHeight(root.left)
            if leftHeight == -1: return -1

            # check if right sub tree is balanced
            rightHeight = dfsHeight(root.right)
            if rightHeight == -1: return -1

            # check if current tree is balance
            if abs(leftHeight - rightHeight) > 1: return -1
            else: return max(leftHeight, rightHeight) + 1

        return dfsHeight(root) != -1