### method:dfs

# time complexity: O(N)
# space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def hasCommonValue(n1, n2):
            if n1 is None and n2 is None:
                return True
            elif n1 and n2:
                if n1.val != n2.val:
                    return False
                else:
                    leftIsCommon = hasCommonValue(n1.left, n2.left)
                    rightIsCommon = hasCommonValue(n1.right, n2.right)
                    return leftIsCommon and rightIsCommon
            else:
                return False
        return hasCommonValue(p, q)