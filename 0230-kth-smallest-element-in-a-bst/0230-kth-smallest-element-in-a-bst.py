# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


### method1: dfs
# time complexity: O(N)
# space complexity: O(N)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            if not root:
                return []
            return dfs(root.left)+[root.val]+dfs(root.right)
        return dfs(root)[k-1]


### method2: binary search

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def countNode(root):
            if not root: return 0
            return 1 + countNode(root.left) + countNode(root.right)
        
        cnt = countNode(root.left)
        if cnt + 1 == k:
            return root.val
        elif cnt + 1 > k:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - cnt - 1)